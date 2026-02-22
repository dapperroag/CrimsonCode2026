import sympy as sp
from .base import BaseSolver

#Returns: sympify object
class AlgebraSolver(BaseSolver):
    def solve(self, user_input: str):
        clean_input = self.cleanse_input(user_input)

        #We are dealing with an equation
        if "=" in clean_input:
            parts = clean_input.split("=")
            left_side = sp.sympify(parts[0])
            right_side = sp.sympify(parts[1])
            equation = sp.Eq(left_side, right_side)
        #Dealing with an expression
        else:
            equation = sp.sympify(clean_input)

        vars = self.get_variables(equation)

        if not vars:
            solution = equation.evalf()
            print(solution)
            return solution
        else:
            solution = sp.solve(equation, vars)
            print(solution)
            return solution
