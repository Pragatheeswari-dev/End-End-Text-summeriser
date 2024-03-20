
from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummerizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI() # Create a FastAPI app

# Define the index route to redirect to the documentation page
@app.get("/", tags=["authentication"]) # Define the route
async def index(): # Define the route handler
    return RedirectResponse(url="/docs") # Redirect to the documentation page of the API


# Define the training route to train the model
@app.get("/train") # Define the route   
async def training(): # Define the route handler
    try: # Try block to handle the exception
        os.system("python main.py") # Execute the training/main.py script
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    


# Define the prediction route to predict the summary of the given text
@app.post("/predict") # Define the route
async def predict_route(text):  # Define the route handler
    try:

        obj = PredictionPipeline()  # Create an object of the PredictionPipeline class
        text = obj.predict(text) # Predict the summary of the given text
        return text
    except Exception as e:
        raise e
    
# Define the main function to run the FastAPI app through uvicorn server to interact with the API
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080) # Run the FastAPI app