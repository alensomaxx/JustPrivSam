/* A retail shop wants to keep track of its total sales for a specific period. They need a program that allows them to input the sales amount for each transaction and calculate the total sales.
Your task is to write a program to calculate and display the total sales amount of a shop. The shop sells various items, and the sales amount of each item is provided as input. Your program should maintain a record of the total sales across all instances of the class using static data members and static member functions.
Company Tags: Deloitte 
Input format :

The first line of input contains an integer, n, representing the number of sales instances.
The next n lines contain the sales amount made by each instance as double values.
Output format :
The output consists of a single line displaying the total sales amount of the shop as a double value rounded to two decimal places.

Refer to the sample output for the formatting specifications.
Code constraints :

The number of sales instances should not exceed 100.

Each sales amount should be a positive double value.
Sample test cases :
Input 1 :

3
100.5
50.75
75.25

Output 1 :

Total Sales: 226.50

Input 2 :

4
25.5
30.75
15.25
20.5

Output 2 :

Total Sales: 92.00*/


#include <iostream>
#include <iomanip> // For setting precision
using namespace std;

class Shop {
private:
    static double totalSales; // Static data member to hold total sales

public:
    // Static member function to add a sale
    static void addSale(double amount) {
        totalSales += amount;
    }

    // Static member function to get total sales
    static double getTotalSales() {
        return totalSales;
    }
};

// Initialize static member variable
double Shop::totalSales = 0.0;

int main() {
    int n;
    cout << "Enter number of sales instances: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        double amount;
        cout << "Enter sales amount for instance " << i + 1 << ": ";
        cin >> amount;
        Shop::addSale(amount); // Adding each sale to the total sales
    }

    // Displaying the total sales with 2 decimal places
    cout << fixed << setprecision(2) << "Total Sales: " << Shop::getTotalSales() << endl;

    return 0;
}
