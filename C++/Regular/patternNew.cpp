#include <iostream>

using namespace std;

void printPattern(int n) {
    // Print the top half of the pattern
    for (int i = 1; i <= n; i++) {
        // Print leading spaces
        for (int j = 1; j <= n - i; j++) {
            cout << "  ";
        }

        // Print the left side of the pattern
        for (int j = 1; j <= i - 1; j++) {
            cout << j << "  ";
        }

        // Print the center asterisk
        cout << "* ";

        // Print the right side of the pattern
        for (int j = i - 1; j >= 1; j--) {
            cout << j << "  ";
        }

        cout << endl;
    }

    // Print the bottom half of the pattern
    for (int i = n - 1; i >= 1; i--) {
        // Print leading spaces
        for (int j = 1; j <= n - i; j++) {
            cout << "  ";
        }

        // Print the left side of the pattern
        for (int j = 1; j <= i - 1; j++) {
            cout << j << "  ";
        }

        // Print the center asterisk
        cout << "* ";

        // Print the right side of the pattern
        for (int j = i - 1; j >= 1; j--) {
            cout << j << "  ";
        }

        cout << endl;
    }
}

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    printPattern(n);

    return 0;
}