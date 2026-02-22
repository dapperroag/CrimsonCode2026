import os
import numpy as np
import sympy as sp
import ast



#Takes input data and puts it into arrays
def input_to_matrix(string) :
    try:
     raw_string = ast.literal_eval(string)
     return np.array(raw_string)
    except Exception as e:
       return f"Error parsing matrix: {e}"


#Records basic information about the matrix for analysis if needed
def reportSteps(A) : 
   report = {
      "original": A.tolist(), #Original matrices
      "is_square": A.shape[0] == A.shape[1], #If it's a square matrix
      "rank": np.lingalg.matrix_rank(A), #Dimensionality of matrix
   }
   if report["is_square"]:
      report["determinant"] = round(np.lingalg.det(A), 2) #Gives determinant if it exists

      return report


#Simple dot product
def dotProd(A, B) :
    prod = np.dot(A, B)
    return prod


#Simple inverse --requires square matrix
def inverse(A) :
   det = np.linalg.det(A)
   if det != 0: #Will not compute is det DNE
      inv = np.linalg.inv(A) 
   else:
      print("Matrix is singular, has no inverse")





r = np.array([59,12])
p = np.array([4,7])

print(r)