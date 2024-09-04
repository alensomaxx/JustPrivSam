/*Let's imagine you are working on a program that involves complex numbers. You have been assigned the task of creating a ComplexNumber class to handle complex number operations. The ComplexNumber class has member variables: real and imaginary, representing the real and imaginary parts of a complex number.


To enhance the functionality of the ComplexNumber class, you need to implement a friend function named multiply(). This function takes two ComplexNumber objects as arguments and returns their multiplication result.


Now, let's consider a scenario where you are designing a scientific calculator application. You want to provide complex number multiplication functionality to the calculator's users. Your task is to implement the ComplexNumber class and the multiply() function, allowing users to multiply two complex numbers.


Note: This is a sample question asked in Infosys recruitment.
Input format :

The first line consists of two space-separated double values, representing the real and imaginary parts of the first complex number.

The second line consists of two space-separated double values, representing the real and imaginary parts of the second complex number.
Output format :

The output displays the result of the multiplication in the format "a + bi", where a is the real part and b is the imaginary part.


Refer to the sample output for the formatting specifications.
Code constraints :

Real and imaginary parts of the complex numbers are of double datatype.

-400.0 ≤ input values ≤ 400.0
Sample test cases :
Input 1 :

2.0 2.0
1.2 2.2

Output 1 :

-2 + 6.8i

Input 2 :

1.5 9.0
3.6 -0.9

Output 2 :

13.5 + 31.05i
*/

#include <iostream>
using namespace std;

class ComplexNumber {
private:
    double real;
    double imaginary;

public:
    // Constructor to initialize complex number
    ComplexNumber(double r = 0, double i = 0) : real(r), imaginary(i) {}

    // Friend function to multiply two ComplexNumber objects
    friend ComplexNumber multiply(const ComplexNumber &c1, const ComplexNumber &c2);

    // Function to display the complex number in the form "a + bi"
    void display() const {
        cout << real;
        if (imaginary >= 0)
            cout << " + " << imaginary << "i";
        else
            cout << " - " << -imaginary << "i";
    }
};

// Function to multiply two complex numbers
ComplexNumber multiply(const ComplexNumber &c1, const ComplexNumber &c2) {
    double realPart = (c1.real * c2.real) - (c1.imaginary * c2.imaginary);
    double imaginaryPart = (c1.real * c2.imaginary) + (c1.imaginary * c2.real);
    return ComplexNumber(realPart, imaginaryPart);
}

int main() {
    double r1, i1, r2, i2;

    // Input real and imaginary parts for the first complex number
    cin >> r1 >> i1;
    ComplexNumber c1(r1, i1);

    // Input real and imaginary parts for the second complex number
    cin >> r2 >> i2;
    ComplexNumber c2(r2, i2);

    // Multiply the two complex numbers
    ComplexNumber result = multiply(c1, c2);

    // Display the result
    result.display();

    return 0;
}
