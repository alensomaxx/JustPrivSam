/*Create a class to store complex numbers. 
It should have three constructors: one with no parameters, 
one with two parameters (real and imaginary parts), 
and one copy constructor. 
The class should also have a function to add two complex numbers.*/

#include <iostream>
using namespace std;

class Complex {
public:
    // Constructors
    Complex() : real(0), imag(0) {} // Default constructor
    Complex(double r, double i) : real(r), imag(i) {} // Constructor with real and imaginary parts
    Complex(const Complex& other) : real(other.real), imag(other.imag) {} // Copy constructor

    // Function to add two complex numbers
    Complex add(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }

    // Function to print the complex number in the format "a + bi" or "a - bi"
    void print() const {
        std::cout << real << " ";
        if (imag >= 0)
            std::cout << "+ " << imag << "i" << std::endl;
        else
            std::cout << "- " << -imag << "i" << std::endl;
    }

private:
    double real;
    double imag;
};

int main() {
    double n1, m1, n2, m2;

    // Input for the first complex number
    cout << "Enter the real and imaginary part of the first complex number: ";
    cin >> n1 >> m1;

    // Input for the second complex number
    cout << "Enter the real and imaginary part of the second complex number: ";
    cin >> n2 >> m2;

    // Create two complex numbers
    Complex c1(n1, m1);
    Complex c2(n2, m2);

    // Add the two complex numbers
    Complex sum = c1.add(c2);

    // Display the result
    cout << "The sum is: ";
    sum.print();

    return 0;
}
 // 2.0 3.0
 // 4.0 -5.0

 // 6 + -2i