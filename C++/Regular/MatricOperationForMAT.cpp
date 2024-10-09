/*Create a class MAT of size m X n.
Define all possible matrix operations for MAT type objects. 

INPUT
Enter the number of rows and columns for the first matrix: 2 2
Enter the elements of the matrix (2 x 2):
1 2
3 4
Enter the number of rows and columns for the second matrix: 2 2
Enter the elements of the matrix (2 x 2):
5 6
7 8


OUTPUT

Matrix 1:
1 2
3 4
Matrix 2:
5 6
7 8
Sum of matrices:
6 8
10 12
Difference of matrices:
-4 -4
-4 -4
Product of matrices:
19 22
43 50
Enter scalar value to multiply with first matrix: 3
Scalar multiplication result:
3 6
9 12

*/

#include <iostream>
#include <vector>

using namespace std;

class MAT {
private:
    int m, n; // Dimensions of the matrix
    vector<vector<int>> mat; // 2D vector to store the matrix elements

public:
    // Constructor to initialize matrix dimensions and set all elements to 0
    MAT(int rows, int cols) {
        m = rows;
        n = cols;
        mat.resize(m, vector<int>(n, 0));
    }

    // Getter methods to access the private member variables
    int getRows() const {
        return m;
    }

    int getCols() const {
        return n;
    }

    // Function to input the matrix elements
    void inputMatrix() {
        cout << "Enter the elements of the matrix (" << m << " x " << n << "):\n";
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> mat[i][j];
            }
        }
    }

    // Function to display the matrix elements
    void displayMatrix() const {
        cout << "Matrix (" << m << " x " << n << "):\n";
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cout << mat[i][j] << " ";
            }
            cout << endl;
        }
    }

    // Addition of two matrices
    MAT operator+(const MAT& other) {
        if (m != other.m || n != other.n) {
            cerr << "Matrix dimensions do not match for addition!\n";
            exit(1);
        }
        MAT result(m, n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result.mat[i][j] = mat[i][j] + other.mat[i][j];
            }
        }
        return result;
    }

    // Subtraction of two matrices
    MAT operator-(const MAT& other) {
        if (m != other.m || n != other.n) {
            cerr << "Matrix dimensions do not match for subtraction!\n";
            exit(1);
        }
        MAT result(m, n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result.mat[i][j] = mat[i][j] - other.mat[i][j];
            }
        }
        return result;
    }

    // Multiplication of two matrices
    MAT operator*(const MAT& other) {
        if (n != other.m) {
            cerr << "Matrix dimensions do not allow multiplication!\n";
            exit(1);
        }
        MAT result(m, other.n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < other.n; j++) {
                result.mat[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    result.mat[i][j] += mat[i][k] * other.mat[k][j];
                }
            }
        }
        return result;
    }

    // Scalar multiplication
    MAT operator*(int scalar) {
        MAT result(m, n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result.mat[i][j] = mat[i][j] * scalar;
            }
        }
        return result;
    }
};

int main() {
    int m, n;

    // Input for the first matrix
    cout << "Enter the number of rows and columns for the first matrix: ";
    cin >> m >> n;
    MAT matrix1(m, n);
    matrix1.inputMatrix();

    // Input for the second matrix
    cout << "Enter the number of rows and columns for the second matrix: ";
    cin >> m >> n;
    MAT matrix2(m, n);
    matrix2.inputMatrix();

    // Display matrices
    cout << "Matrix 1:" << endl;
    matrix1.displayMatrix();

    cout << "Matrix 2:" << endl;
    matrix2.displayMatrix();

    // Matrix addition
    MAT sum = matrix1 + matrix2;
    cout << "Sum of matrices:" << endl;
    sum.displayMatrix();

    // Matrix subtraction
    MAT difference = matrix1 - matrix2;
    cout << "Difference of matrices:" << endl;
    difference.displayMatrix();

    // Matrix multiplication
    if (matrix1.getCols() == matrix2.getRows()) {  // Only multiply if dimensions allow
        MAT product = matrix1 * matrix2;
        cout << "Product of matrices:" << endl;
        product.displayMatrix();
    } else {
        cout << "Matrix dimensions do not allow multiplication!" << endl;
    }

    // Scalar multiplication
    int scalar;
    cout << "Enter scalar value to multiply with first matrix: ";
    cin >> scalar;
    MAT scalarProduct = matrix1 * scalar;
    cout << "Scalar multiplication result:" << endl;
    scalarProduct.displayMatrix();

    return 0;
}
