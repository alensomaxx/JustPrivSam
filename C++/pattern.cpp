/*
                1
            1   2   1
        1   2   3   2   1
    1   2   3   4   3   2   1
1   2   3   4   5   4   3   2   1
    1   2   3   4   3   2   1
        1   2   3   2   1
            1   2   1  
                1

Print this pattern for inputed by the user!
with the concept of op!


                *
            1   *   1
        *   2   *   2   *
    1   *   3   *   3   *   1
*   2   *   4   *   4   *   2   *
    1   *   3   *   3   *   1
        *   2   *   2   *
            1   *   1  
                *
Updated pattern
*/

#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    // Print the top half of the pattern
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << "  ";
        }
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        for (int j = i - 1; j >= 1; j--) {
            cout << j << " ";
        }
        cout << endl;
    }

    // Print the bottom half of the pattern
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << "  ";
        }
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        for (int j = i - 1; j >= 1; j--) {
            cout << j << " ";
        }
        cout << endl;
    }

    return 0;
}