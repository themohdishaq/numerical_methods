import numpy as np
from scipy.optimize import fsolve

# Define the function
def equation(x):
    return 4*x**2 - np.exp(x)

# Initial guesses for roots
initial_guesses = [-1, 0, 1]

# Solve for x
solutions = fsolve(equation, initial_guesses)
print(solutions)
