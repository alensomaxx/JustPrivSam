#include <iostream>

using namespace std;

class LengthConverter {
public:
    float sumInMeters(float feet, float meters) {
        float totalMeters = feet * 0.3048 + meters;
        return totalMeters;
    }

    float sumInFeet(float feet, float meters) {
        float totalFeet = feet + meters * 3.28084;
        return totalFeet;
    }
};

int main() {
    LengthConverter converter;
    float feet, meters;

    cout << "Enter the value in feet: ";
    cin >> feet;
    cout << "Enter the value in meters: ";
    cin >> meters;

    float totalMeters = converter.sumInMeters(feet, meters);
    cout << "The sum in meters is: " << totalMeters << endl;

    float totalFeet = converter.sumInFeet(feet, meters);
    cout << "The sum in feet is: " << totalFeet << endl;

    return 0;
}