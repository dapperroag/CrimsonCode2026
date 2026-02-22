from .base import BaseSolver

class CalculusSolver(BaseSolver):
    def integrate(self, user_input: str):
        clean_input = self.cleanse_input(user_input)
        expr = self.to_sp_object(clean_input)

        

        
        
