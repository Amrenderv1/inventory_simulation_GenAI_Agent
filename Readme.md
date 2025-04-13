## Inventory Simulation and Analysis Application
This FastAPI application simulates inventory data, calculates recommended order quantities, and provides insights into inventory management. It uses OpenAI's language models for advanced simulation and analysis based on the given parameters.

## Features
Simulate inventory over a defined number of days.

Calculate recommended order quantities based on daily usage, lead time, and other parameters.

Analyze the simulation data to identify stockouts, reorder points, trends, and recommendations.

## Requirements
To run the application, you need to have Python 3.7+ installed along with the following packages:

FastAPI: Web framework to build APIs.

Uvicorn: ASGI server to run the FastAPI application.

OpenAI: OpenAI API to interact with GPT models.

Pydantic: Data validation and parsing.

LangChain: Used for integrating agents with OpenAI's models.

python-dotenv: To load environment variables from a .env file.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/inventory-simulation.git
cd inventory-simulation
Create a virtual environment:

bash
Copy
Edit
python -m venv .venv
Activate the virtual environment:

On Windows:

bash
Copy
Edit
.\.venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source .venv/bin/activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root directory and add your OpenAI API key:

bash
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
Running the Application
Start the FastAPI application:

bash
Copy
Edit
uvicorn inventory_app:app --reload
Access the API in your browser:
Open your browser and go to:

bash
Copy
Edit
http://127.0.0.1:8000/docs
This will show the interactive API documentation where you can test the endpoints.

API Endpoints
/simulate_inventory
Method: POST

Description: Simulate inventory data for the given parameters.