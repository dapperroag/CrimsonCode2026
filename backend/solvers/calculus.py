import sympy as sp
from .base import BaseSolver

#limitation: only works with variable x
#Returns: prints sympify object
class CalculusSolver(BaseSolver):
    def integrate(self, user_input: str):
        clean_input = self.cleanse_input(user_input)
        expr = self.to_sp_object(clean_input)

        var = self.get_variables(expr)

        result = sp.integrate(expr, sp.Symbol("x"))

        print(result)

    def differentiate(self, user_input: str):
        clean_input = self.cleanse_input(user_input)
        expr = self.to_sp_object(clean_input)
        
        var = self.get_variables(expr)

        result = sp.diff(expr, sp.Symbol("x"))

        print(result)

    #def limit(self, user_input: str): get back to this later
        

        

        
        
