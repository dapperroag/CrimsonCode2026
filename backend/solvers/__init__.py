#This runs once the solvers package is imported
from .base import BaseSolver
from .algebra import AlgebraSolver
from .calculus import CalculusSolver

algebra_solver = AlgebraSolver()
calculus_solver = CalculusSolver()