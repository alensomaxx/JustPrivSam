//program to help implement a ticketing system 
//that allows customers to search for available seats
// Input format :

//The first line of the input consists of the number of seats, n.

//The next line of input consists of n space-separated seat numbers as integers.

//The last line of input is the seat number to be searched (m).
//Output format :

//The output prints the status of the seat availability.


#include <iostream>
using namespace std;

class ArraySearch {
public:
    // Method to check seat availability
    bool searchSeat(int seats[], int n, int seatNumber) {
        for (int i = 0; i < n; i++) {
            if (seats[i] == seatNumber) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    int n;
    cin >> n;  // Read the number of seats

    int seats[n];
    
    // Read the seat numbers
    for (int i = 0; i < n; i++) {
        cin >> seats[i];
    }

    int m;
    cin >> m;  // Read the seat number to search for

    ArraySearch arraySearch;
    
    // Check if the seat is available
    if (arraySearch.searchSeat(seats, n, m)) {
        cout << "Seat is available" << endl;
    } else {
        cout << "Seat is not available" << endl;
        cout << "Try Again later" << endl;
    }

    return 0;
}


//5
//50 40 10 20 30
//20