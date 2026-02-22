import numpy as np
import sympy as sp
from google import genai

import solvers

user_input = input()

algebra_solver = solvers.algebra_solver

result = algebra_solver.solve(user_input)


