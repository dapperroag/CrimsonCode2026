#This runs once the solvers package is imported
from .base import BaseSolver
from .algebra import AlgebraSolver

algebra_solver = AlgebraSolver()

print("Solvers included.")