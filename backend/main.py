import numpy as np
import sympy as sp
from google import genai

import solvers

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
    # call your teammate's function here
    result = data.string.upper()  # example logic
    return {"result": result}

user_input = input()

algebra_solver = solvers.algebra_solver
calculus_solver = solvers.calculus_solver

result = calculus_solver.integrate(user_input)


