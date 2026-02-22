import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

class BaseSolver():
    def __init__(self):
        self.transformations = standard_transformations + (implicit_multiplication_application,)
        self.allowed_funcs = {
            'x': sp.symbols('x', real = True),
            'sin': sp.sin,
            'cos': sp.cos,
            'tan': sp.tan,
            'sqrt': sp.sqrt,
            'integrate': sp.integrate,
            'diff': sp.diff,
            'abs': sp.Abs,
            'ln': sp.log
        }
    
    def cleanse_input(self, user_input: str):
        clean_string = user_input.replace("^", "**")
        return clean_string
    
    def to_sp_object(self, user_input: str):
        return sp.parse_expr(self.cleanse_input(str),self.allowed_funcs,self.transformations)
    
    def get_variables(self, sp_object):
        var = sp_object.atoms(sp.Symbol)
        return var
    
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

        #There are no symbols/variables in this input
        if not vars:
            solution = equation.evalf()
            print(solution)
            return solution
        else:
            #Try to solve with variables and then evaluate numerically
            try:
                solution = sp.solve(equation, vars)
            except Exception as e:
                print("Could not solve: ", e)
            solution = sp.solve(equation, vars)
            print(solution)
            return solution
