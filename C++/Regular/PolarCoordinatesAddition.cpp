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


*/

#include <iostream>
#include <cmath>
using namespace std;

class Polar{
    private: 
        double radius;
        double angle;
    public:
        Polar(double radius = 0, double angle=0) : radius(radius),angle(angle){}

        Polar operator+(const Polar& other )const {
            double x1 = radius*cos(angle);
            double y1 = radius*sin(angle);
            double x2 = other.radius*sin(other.angle);
            double y2 = other.radius*cos(other.angle);

            double xSum = x1 + x2;
            double ySum = y1 + y2;

            double newRadius = sqrt(xSum * xSum + ySum * ySum);
            double newAngle = atan2(ySum, xSum);

            return Polar(newRadius, newAngle);

        }
        void print() const {
        cout << "Radius: " << radius << ", Angle: " << angle << endl;
    }
};

int main(){
    int a , b;
    int aa,bb;
    cout<<"Enter the 1st radius:";cin>>a;
    cout<<"Enter the 1st degree:";cin>>b;
    cout<<"Enter the 2nd radius:";cin>>aa;
    cout<<"Enter the 2nd degree:";cin>>bb;
    

    Polar p1(a, b);
    Polar p2(aa, bb);

    Polar p3 = p1 + p2;

    cout << "Point 1: ";
    p1.print();

    cout << "Point 2: ";
    p2.print();

    cout << "Sum of points: ";
    p3.print();

    return 0;
}