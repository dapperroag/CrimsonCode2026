import numpy as np
import sympy as sp
from google import genai

import solvers

user_input = input()

algebra_solver = solvers.algebra_solver
calculus_solver = solvers.calculus_solver

result = calculus_solver.integrate(user_input)


