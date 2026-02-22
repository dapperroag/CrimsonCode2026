from .base import BaseSolver

class AlgebraSolver(BaseSolver):
    def solve(self, user_input: str):
        user_input = self.cleanse_input(user_input)
        expr = self.to_sp_object(user_input)
        print(expr)