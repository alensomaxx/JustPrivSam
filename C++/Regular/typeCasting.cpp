/*Write a program that includes two classes: one with a private member representing 
meters and another representing feet. Implement type casting to convert feet to 
meters using the private member of the class representing meters.*/

#include <iostream>

using namespace std;

class Meters {
private:
    double meters;

public:
    Meters(double meters) : meters(meters) {}

    double getMeters() const {
        return meters;
    }

    double convertToFeet() const {
        return meters * 3.28084;
    }
};

class Feet {
private:
    double feet;

public:
    Feet(double feet) : feet(feet) {}

    double getFeet() const {
        return feet;
    }

    Meters convertToMeters() const {
        return Meters(feet / 3.28084);
    }
};

int main() {
    double m;
    double f;
    cout<<"Enter Meters: "; cin>> m;
    cout<<"Enter Feets: "; cin>> f;
    
    Meters meters(m);
    Feet feet(f);

    cout << "Meters: " << meters.getMeters() << endl;
    cout << "Feet: " << feet.getFeet() << endl;
    cout<<"YESS!!!"<<endl;
    cout<<"YESS!!!"<<endl;

    cout << "Meters to feet: " << meters.convertToFeet() << " feet" << endl;
    cout << "Feet to meters: " << feet.convertToMeters().getMeters() << " meters" << endl;

    return 0;
}