import sympy as sp

class BaseSolver():
    def cleanse_input(self, user_input: str):
        clean_string = user_input.replace("^", "**")
        return clean_string
    
    def to_sp_object(self, clean_string: str):
        return sp.sympify(clean_string)
    
    def parse_string(self, user_input: str):
        if "gral" in user_input:
            hello = 10

