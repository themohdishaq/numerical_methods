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

def bisection_method(fun, a, b, tol=1e-6, max_iter=100):
    if fun(a) * fun(b) >= 0:
        return None
    for _ in range(max_iter):
        c = (a +b) / 2
        if fun(c) == 0 or (b -a) < tol:
            return c
        if fun(c) * fun(a) < 0:
            b = c
        else:
            a = c
    return (a + b)/2

# Use bisection method to find the root

root1 = bisection_method(equation, -1, 0)

root2 = bisection_method(equation, 0, 1)
    
print("root1: %d root2: %d ", root1,  root2)