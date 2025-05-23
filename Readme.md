## Inventory Simulation API using FastAPI & OpenAI GPT
Inventory Simulation and Analysis Application
This FastAPI application simulates inventory data, calculates recommended order quantities, and provides insights into inventory management. 
It uses OpenAI's language models for advanced simulation and analysis based on the given parameters uisng GENAI agents.



Features
Simulate inventory over a defined number of days.
Calculate recommended order quantities based on daily usage, lead time, and other parameters.
Analyze the simulation data to identify stockouts, reorder points, trends, and recommendations & keyinisghts uisng langchain agents.



Requirements
To run the application, you need to have Python 3.7+ installed along with the following packages:

FastAPI: Web framework to build APIs.
Uvicorn: ASGI server to run the FastAPI application.
OpenAI: OpenAI API to interact with GPT models.
Pydantic: Data validation and parsing.
LangChain: Used for integrating agents with OpenAI's models.
python-dotenv: To load environment variables from a .env file.

## Features
Simulate daily inventory over a given period
Calculate recommended reorder quantity using dynamic parameters
Generate daily-level inventory insights using GPT
Analyze inventory simulation to detect stockouts, reorder opportunities, and optimization trends
API built with FastAPI for easy integration and testing

## Tech Stack
Python 3.9+
FastAPI
OpenAI GPT-3.5
Uvicorn (ASGI server)
Pandas, Matplotlib

## Inventory Simulation API using FastAPI & OpenAI GPT

This application simulates and analyzes inventory data using OpenAI's GPT model via a RESTful API built with FastAPI. It is ideal for inventory planners, supply chain analysts, and developers looking to automate reorder quantity recommendations and trend insights using natural language processing.

---

## Features

- Simulate daily inventory over a given period
- Calculate recommended reorder quantity using dynamic parameters
- Generate daily-level inventory insights using GPT
- Analyze inventory simulation to detect stockouts, reorder opportunities, and optimization trends
- API built with FastAPI for easy integration and testing

---

## Core Packages Used
## Package	Purpose
fastapi	To build the REST API
uvicorn	ASGI server to run FastAPI
openai	To interact with OpenAI's GPT models
pandas	Data manipulation and formatting
matplotlib	Plotting/visualization support (optional, not used directly yet)
python-dotenv	To load environment variables from a .env file

## How to Run the App

### 1. Clone the Repository
https://github.com/Amrenderv1/inventory_simulation_GenAI_Agent.git



cd inventory-simulation-api

 
 
