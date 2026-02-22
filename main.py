import numpy as np
import scipy as sp
import reactpy
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message": "FastAPI Loaded"}


    