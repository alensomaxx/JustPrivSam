/*Create a class FLOAT that contains ine float data member. 
Overload all the four arithematic operators so that they operate 
on the objects of FLOAT*/

#include <iostream>
using namespace std;

class FLOAT {
private:
    float value;  // Data member to store the float value
public:
    // Constructor
    FLOAT(float value = 0.0) : value(value) {}

    // Overload + operator
    FLOAT operator+(const FLOAT& other) const {
        return FLOAT(value + other.value);
    }

    // Overload - operator
    FLOAT operator-(const FLOAT& other) const {
        return FLOAT(value - other.value);
    }

    // Overload * operator
    FLOAT operator*(const FLOAT& other) const {
        return FLOAT(value * other.value);
    }

    // Overload / operator (with a check for division by zero)
    FLOAT operator/(const FLOAT& other) const {
        if (other.value == 0) {
            cout << "Error: Division by zero!" << endl;
            return FLOAT();  // Return default value
        }
        return FLOAT(value / other.value);
    }

    // Function to print the value of the FLOAT object
    void print() const {
        cout << value << endl;
    }
};

int main() {
    float a,b;
    cout << "Enter the 1st Value: "; 
    cin >> a;
    cout << "Enter the 2nd Value: "; 
    cin >> b;

    

    FLOAT f1(a), f2(b);  // Create two FLOAT objects

    FLOAT f3 = f1 + f2;  // Add f1 and f2
    FLOAT f4 = f1 - f2;  // Subtract f2 from f1
    FLOAT f5 = f1 * f2;  // Multiply f1 and f2
    FLOAT f6 = f1 / f2;  // Divide f1 by f2

    cout << "f1 + f2 = "; f3.print();
    cout << "f1 - f2 = "; f4.print();
    cout << "f1 * f2 = "; f5.print();
    cout << "f1 / f2 = "; f6.print();

    return 0;
}
