/*
123454321
1234 4321
123   321
12     21
1       1
Print this pattern using classe and relative things

*/


#include <iostream>

using namespace std;

class Pattern {
public:
    int size;

    Pattern(int n) {
        size = n;
    }

    void print() {
        for (int i = size; i >= 1; i--) {
            for (int j = 1; j <= size - i; j++) {
                cout << " ";
            }
            for (int k = i; k >= 1; k--) {
                cout << k;
            }
            cout << " ";
            for (int k = 2; k <= i; k++) {
                cout << k;
            }
            cout << endl;
        }
    }
};

int main() {
    int n;
    cout << "Enter the size of the pattern: ";
    cin >> n;

    Pattern pattern(n);
    pattern.print();

    return 0;
}