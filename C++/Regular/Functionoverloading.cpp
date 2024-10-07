#include <iostream>
using namespace std;

float sumInMeters(float feet, float meters){
    float totalmeters = feet*0.3048+meters;
    return totalmeters;
}

float sumInFeet(float feet, float meters){
    float totalFeet = meters*3.28084+feet;
    return totalFeet;
}

int main(){
    float feet, meters;

    cout<<"Enter the value in feets: ";cin>>feet;
    cout<<"Enter the value in Meters: ";cin>>meters;

    float totalMeters = sumInMeters(feet, meters);
    cout << "The sum in meters is: " << totalMeters << endl;

    float totalFeet = sumInFeet(feet, meters);
    cout << "The sum in feet is: " << totalFeet << endl;
    


    return 0;
}