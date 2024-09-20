/* Single File Programming Question

Problem Statement


You are tasked with designing a simple airline reservation system for a small airline company. The system should allow the airline to manage and provide information about their flight destinations and the number of flights available to each destination.


You need to implement a class named Airline with the following functions:

    void initialize(): Initializes the airline's system with no destinations and no flights.
    void addDestination (int, int): Adds a new destination and the number of flights available to that destination. The system can store up to 100 destinations.
    int checkFlights (int): Checks and returns the number of available flights to a specific destination. If the destination is not found, it returns -1.

Input format :

The first input consists of an integer n, representing the number of destinations the airline wants to add.

The next n lines consist of two space-separated integers for each destination: destination code and number of flights available.

The last input consists of an integer search for destination Q.
Output format :

The output displays the following one of the format:

If the search destination is found in the system, it prints the number of available flights to that destination.

If the search destination is not found in the system, it prints "Destination not found."


Refer to the sample output for the formatting specifications.
Code constraints :

In this scenario, the test cases fall under the following constraints:

1 ≤ n ≤ 50
Sample test cases :
Input 1 :

3
101 5
102 3
103 7
102

Output 1 :

3

Input 2 :

4
201 8
202 4
203 6
204 2
205

Output 2 :

Destination not found

*/


#include <iostream>

using namespace std;

const int MAX_DESTINATIONS = 100;

class Airline {
public:
    void initialize() {
        numDestinations = 0;
        for (int i = 0; i < MAX_DESTINATIONS; i++) {
            destinations[i].code = 0;
            destinations[i].numFlights = 0;
        }
    }

    void addDestination(int code, int numFlights) {
        if (numDestinations < MAX_DESTINATIONS) {
            destinations[numDestinations].code = code;
            destinations[numDestinations].numFlights = numFlights;
            numDestinations++;
        }
    }

    int checkFlights(int destinationCode) {
        for (int i = 0; i < numDestinations; i++) {
            if (destinations[i].code == destinationCode) {
                return destinations[i].numFlights;
            }
        }
        return -1;
    }

private:
    struct Destination {
        int code;
        int numFlights;
    };

    Destination destinations[MAX_DESTINATIONS];
    int numDestinations;
};

int main() {
    Airline airline;
    airline.initialize();

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int code, numFlights;
        cin >> code >> numFlights;
        airline.addDestination(code, numFlights);
    }

    int searchDestination;
    cin >> searchDestination;

    int availableFlights = airline.checkFlights(searchDestination);

    if (availableFlights != -1) {
        cout << availableFlights << endl;
    } else {
        cout << "Destination not found" << endl;
    }

    return 0;
}


