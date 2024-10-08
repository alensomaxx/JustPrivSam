/*Design a class polar which describes a point in the plane 
using polar coordinates radius and angle. A point in polar 
coordinates is shown 
Use the overloaded + operator to add two objects of polar 

Note that we cannot add polar values of two points directly. 
This requires first the conversion of points into rectangluar co-ordinates, then adding 
the corresponding rectangluar co-ordinates and finally converting the result back into 
polar co-ordinates. you need to use the following trignometric formulae:
x=r*cos(a)
y=r*sin(a)
a=atan(y/x)
r=sqrt(x*x + y*y)


Test Case 1: 
Radius = 3, Angle = 45 degrees
Radius = 2, Angle = 60 degrees
Expected Output:
Radius ≈ 4.36, Angle ≈ 51.32 degrees
*/

#include <iostream>
#include <cmath>
using namespace std;

class Polar {
private:
    double radius;
    double angle;  // Angle in radians
public:
    // Constructor with default parameters
    Polar(double radius = 0, double angle = 0) : radius(radius), angle(angle) {}

    // Overloaded + operator to add two Polar objects
    Polar operator+(const Polar& other) const {
        // Convert angles from degrees to radians for calculations
        double angle1Rad = angle * M_PI / 180.0;
        double angle2Rad = other.angle * M_PI / 180.0;

        // Convert Polar coordinates to Rectangular (x, y)
        double x1 = radius * cos(angle1Rad);
        double y1 = radius * sin(angle1Rad);
        double x2 = other.radius * cos(angle2Rad);
        double y2 = other.radius * sin(angle2Rad);

        // Add the rectangular coordinates
        double xSum = x1 + x2;
        double ySum = y1 + y2;

        // Convert back to Polar coordinates
        double newRadius = sqrt(xSum * xSum + ySum * ySum);
        double newAngle = atan2(ySum, xSum) * 180.0 / M_PI; // Convert radians to degrees

        return Polar(newRadius, newAngle);
    }

    // Function to print the Polar coordinates
    void print() const {
        cout << "Radius: " << radius << ", Angle: " << angle << " degrees" << endl;
    }
};

int main() {
    double r1, theta1, r2, theta2;
    
    cout << "Enter the 1st radius: "; cin >> r1;
    cout << "Enter the 1st angle (in degrees): "; cin >> theta1;
    cout << "Enter the 2nd radius: "; cin >> r2;
    cout << "Enter the 2nd angle (in degrees): "; cin >> theta2;

    // Create two Polar objects
    Polar p1(r1, theta1);
    Polar p2(r2, theta2);

    // Add the two Polar objects
    Polar p3 = p1 + p2;

    // Display the results
    cout << "Point 1: ";
    p1.print();

    cout << "Point 2: ";
    p2.print();

    cout << "Sum of points: ";
    p3.print();

    return 0;
}
