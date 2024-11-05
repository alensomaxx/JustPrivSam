/*Create a base class called shape. Use this class to store two double type values that could
be used to compute the area of figure. Derive two specific classes called triangle and rectangle 
from base shape. Add to the base class, a member function get_data() to initalize base class 
data memebvers and another member function display_area() to compute and display the area 
of figure. Make display_area() as a virtual funtion and redefine this function in the 
derived classes to suit their requiremements.

Using these three classes, design a program that will accept dimenesions of a traingle or a rectangle
interactively, and and display the area.
Remember the two values given as input wil be treated as length of two sides in the case of 
rectangle and as base and height in the case of triangles,and used as follows:
Area of rectangle = x*y 
Area of triangle = 1/2 *x*y  
*/

#include <iostream>

using namespace std;

class Shape {
public:
    double x, y;

    virtual void get_data() = 0;
    virtual void display_area() = 0;
};

class Triangle : public Shape {
public:
    void get_data() override {
        cout << "Enter base and height of the triangle: ";
        cin >> x >> y;
    }

    void display_area() override {
        double area = 0.5 * x * y;
        cout << "Area of the triangle: " << area << endl;
    }
};

class Rectangle : public Shape {
public:
    void get_data() override {
        cout << "Enter length and width of the rectangle: ";
        cin >> x >> y;
    }

    void display_area() override {
        double area = x * y;
        cout << "Area of the rectangle: " << area << endl;
    }
};

int main() {
    Shape* shape;
    int choice;

    cout << "1. Triangle\n2. Rectangle\nChoose the shape: ";
    cin >> choice;

    if (choice == 1) {
        shape = new Triangle();
    } else if (choice == 2) {
        shape = new Rectangle();
    } else {
        cout << "Invalid choice.\n";
        return 1;
    }

    shape->get_data();
    shape->display_area();

    delete shape;

    return 0;
}
