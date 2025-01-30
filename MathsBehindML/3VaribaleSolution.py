import numpy as np

# Function to get user input for a 3x3 system of equations
def get_user_input():
    print("Enter the coefficients and constant for each equation:")
    
    # Initialize empty lists to store coefficients and constants
    A = []
    B = []
    
    for i in range(3):
        print(f"\nEquation {i+1}:")
        a = float(input("Enter coefficient for x: "))
        b = float(input("Enter coefficient for y: "))
        c = float(input("Enter coefficient for z: "))
        d = float(input("Enter the constant term: "))
        
        # Append coefficients to matrix A
        A.append([a, b, c])
        # Append constant to matrix B
        B.append(d)
    
    # Convert lists to numpy arrays
    A = np.array(A)
    B = np.array(B)
    
    return A, B

# Get user input
A, B = get_user_input()

# Solve the system of equations
try:
    solution = np.linalg.solve(A, B)
    print("\nThe solution is:")
    print(f"x = {solution[0]}")
    print(f"y = {solution[1]}")
    print(f"z = {solution[2]}")
except np.linalg.LinAlgError:
    print("\nThe system of equations has no unique solution (either no solution or infinitely many solutions).")