import openai
import os
import pandas as pd
from datetime import timedelta, datetime
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI

# Load environment variables
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

# Setup LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# FastAPI app initialization
app = FastAPI()

# Define the SimulationParams model to validate incoming data
class SimulationParams(BaseModel):
    current_inventory: int
    daily_usage: intP
    reorder_point: int
    order_quantity: int
    lead_time: int
    num_days: int
    picked: int
    restocked: int
    target_inventory_threshold: int
    target_inventory_param: float
    maximum_quantity: int
    eaches_quantity: int

# ------------------------
# Functions (Simulate Inventory, Calculate Recommended Order Quantity)
# ------------------------

def calculate_recommended_order_quantity(parameters, sum_mpi_quantity):
    """Calculates the recommended order quantity based on given parameters."""
    average_daily_use = max(parameters["daily_usage"], 0)
    target_inventory = min(
        max(average_daily_use * parameters["target_inventory_param"], parameters["target_inventory_threshold"]),
        parameters["maximum_quantity"]
    )
    adjusted_quantity = max(0, target_inventory - max(0, sum_mpi_quantity))
    recommended_quantity = max(1, round(adjusted_quantity / parameters["eaches_quantity"]))
    return recommended_quantity

def simulate_inventory(parameters: dict) -> str:
    new_inventory = parameters['current_inventory'] + parameters['restocked'] - parameters['picked']
    sum_mpi_quantity = new_inventory
    recommended_order = calculate_recommended_order_quantity(parameters, sum_mpi_quantity)

    prompt = f"""
    You are an AI assistant helping with inventory management. Simulate inventory data for the next {parameters['num_days']} days using the following parameters:
    - Starting inventory: {new_inventory}
    - Daily usage: {parameters['daily_usage']}
    - Reorder point: {parameters['reorder_point']}
    - Order quantity: {parameters['order_quantity']}
    - Lead time: {parameters['lead_time']} days
    - Recommended order quantity: {recommended_order}

    For each day, provide the following:
    1. Day number
    2. Remaining inventory after daily usage
    3. Indicate if an order is placed (yes/no)
    4. The inventory level after any incoming orders are delivered
    5. New inventory (calculated as starting_inventory + restocked - picked)
    6. Recommended Order Quantity

    Generate this simulation in a structured table format with columns: "Day", "Inventory Level", "Order Placed", "Post-Order Inventory", "New Inventory", and "Recommended Order Quantity".
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message["content"]

def analyze_simulation(simulation_data: str) -> str:
    prompt = f"""
    Based on the following inventory simulation data:

    {simulation_data}

    Additionally, analyze the results and provide key insights, including:  
    - Number of stockouts and when they occurred  
    - The most optimal reorder day  
    - Trends in inventory fluctuations  
    - Recommended adjustments to inventory management  
    - Evaluation of whether the recommended order quantity aligns with demand patterns  

    Ensure the response is easy to interpret and that the analysis focuses on critical inventory management insights.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message["content"]

# ------------------------
# Define LangChain Tools
# ------------------------

tool_simulate = Tool(
    name="simulate_inventory",
    func=simulate_inventory,
    description="Simulates inventory levels and order placements over time."
)

tool_analyze = Tool(
    name="analyze_simulation",
    func=analyze_simulation,
    description="Analyzes inventory simulation data to provide insights."
)

# Initialize LangChain Agent
agent = initialize_agent(
    tools=[tool_simulate, tool_analyze],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# ------------------------
# FastAPI Endpoints
# ------------------------

@app.post("/simulate-agent")
def simulate_with_agent(params: SimulationParams):
    # Pass parameters to the agent for simulation
    query = f"Simulate inventory with parameters {params.dict()}"
    result = agent.run(query)
    return {"simulation_result": result}

@app.post("/analyze-agent")
def analyze_with_agent(simulation_data: str):
    # Pass simulation data to the agent for analysis
    result = agent.run(f"Analyze the following simulation data: {simulation_data}")
    return {"analysis_result": result}
