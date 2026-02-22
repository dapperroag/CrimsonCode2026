import sympy as sp

class BaseSolver():
    def cleanse_input(self, user_input: str):
        clean_string = user_input.replace("^", "**")
        return clean_string
    
    def to_sp_object(self, user_input: str):
        return sp.sympify(self.cleanse_input(user_input))
    
    def get_variables(self, sp_object):
        var = sp_object.atoms(sp.Symbol)
        return var
