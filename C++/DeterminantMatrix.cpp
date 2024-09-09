/*WAP to find the determinant of a matrix
Matrix should be stored in a class
Calculation should be done in a friend function*/

#include <iostream>

using namespace std;

class Matrix {
public:
    int rows, cols;
    int **data;

    Matrix(int r, int c) {
        rows = r;
        cols = c;
        data = new int*[rows];
        for (int i = 0; i < rows; i++) {
            data[i] = new int[cols];
        }
    }

    void input() {
        cout << "Enter elements of the matrix:\n";
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cin >> data[i][j];
            }
        }
    }

    void display() {
        cout << "Matrix:\n";
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cout << data[i][j] << " ";
            }
            cout << endl;
        }
    }

    ~Matrix() {
        for (int i = 0; i < rows; i++) {
            delete[] data[i];
        }
        delete[] data;
    }
};

int determinant(Matrix &mat) {
    if (mat.rows != mat.cols) {
        cout << "Determinant can only be calculated for square matrices.\n";
        return 0;
    }

    if (mat.rows == 1) {
        return mat.data[0][0];
    }

    int det = 0;
    int sign = 1;
    for (int i = 0; i < mat.rows; i++) {
        Matrix minor(mat.rows - 1, mat.cols - 1);
        for (int j = 1; j < mat.rows; j++) {
            for (int k = 0; k < mat.cols; k++) {
                if (k != i) {
                    minor.data[j - 1][k < i ? k : k - 1] = mat.data[j][k];
                }
            }
        }
        det += sign * mat.data[0][i] * determinant(minor);
        sign *= -1;
    }
    return det;
}

int main() {
    int rows, cols;
    cout << "Enter the number of rows and columns: ";
    cin >> rows >> cols;

    Matrix matrix(rows, cols);
    matrix.input();
    matrix.display();

    int det = determinant(matrix);
    cout << "Determinant of the matrix: " << det << endl;

    return 0;
}
