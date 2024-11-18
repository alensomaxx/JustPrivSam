#include <iostream>

using namespace std;

int main() {
    int a, b;

    cout << "Enter values of a and b: ";
    cin >> a >> b;

    try {
        if (b == 0) {
            throw "Division by zero error";
        } else {
            int result = a / b;
            cout << "Result: " << result << endl;
        }
    } catch (const char* msg) {
        cerr << "Exception caught: " << msg << endl;
    }

    cout << "END" << endl;

    return 0;
}