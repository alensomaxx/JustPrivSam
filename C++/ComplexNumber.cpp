/*Create a class to store complex numbers. 
It should have three constructors: one with no parameters, 
one with two parameters (real and imaginary parts), 
and one copy constructor. 
The class should also have a function to add two complex numbers.*/

#include <iostream>

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

    // Function to print the complex number in the format "a + bi"
    void print() const {
        std::cout << real << " + " << imag << "i" << std::endl;
    }

private:
    double real;
    double imag;
};

int main() {
    Complex c1(2, 3);
    Complex c2(4, 5);

    Complex sum = c1.add(c2);
    sum.print(); // Output: 6 + 8i

    return 0;
}