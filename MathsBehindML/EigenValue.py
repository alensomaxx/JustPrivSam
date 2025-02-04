import numpy as np

def calculate_eigenvalues():
    try:
        # Get matrix dimensions from the user
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        # Ensure the matrix is square
        if rows != cols:
            print("Error: The matrix must be square to compute eigenvalues.")
            return

        # Read matrix elements from the user
        print("Enter the matrix elements row-wise:")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Enter row {i+1} elements separated by spaces: ").split()))
            if len(row) != cols:
                print("Error: Incorrect number of elements in the row.")
                return
            matrix.append(row)

        # Convert the matrix to a NumPy array
        A = np.array(matrix)

        # Calculate eigenvalues
        eigenvalues = np.linalg.eigvals(A)

        # Display the eigenvalues
        print("\nThe eigenvalues of the matrix are:")
        for i, val in enumerate(eigenvalues, 1):
            print(f"Eigenvalue {i}: {val}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


calculate_eigenvalues()