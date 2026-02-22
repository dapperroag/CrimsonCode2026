import numpy as np
import sympy as sp
from google import genai

from backend import solvers

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow browser frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can restrict later
    allow_methods=["*"],
    allow_headers=["*"]
)

class StringRequest(BaseModel):
    string: str

@app.post("/process_string")
async def process_string(data: StringRequest):
    print("Received string:", data.string)  # logs in terminal

    # solving for the result
    solver = solvers.general_solver
    result = solver.solve(data.string)

    # convert result to a string with no parentheses or brackets
    output_string = str(result).replace(")","").replace("(","").replace("[","").replace("]","")

    # Wrap result in JSON
    return {"result": output_string}



