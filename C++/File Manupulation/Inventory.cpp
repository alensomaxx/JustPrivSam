#include <iostream>
#include <fstream>
#include <iomanip> // For setiosflags, setw, and setprecision
#include <string>

using namespace std;

class INVENTORY {
    char name[10];
    int code;
    float cost;
public:
    void readdata(void);
    void writedata(void);
};

// Function to read data from the user
void INVENTORY::readdata(void) {
    cout << "Enter Name: "; 
    cin >> name;
    cout << "Enter Code: "; 
    cin >> code;
    cout << "Enter Cost: "; 
    cin >> cost;
}

// Function to write data to the console
void INVENTORY::writedata(void) {
    cout << setiosflags(ios::left)
         << setw(10) << name
         << resetiosflags(ios::left) // Reset left alignment
         << setiosflags(ios::right)
         << setw(10) << code
         << setw(10) << fixed << setprecision(2) << cost
         << endl;
}

int main() {
    INVENTORY item[3];
    fstream file;

    // Open file for input and output, truncating existing content
    file.open("STOCK.DAT", ios::in | ios::out | ios::trunc | ios::binary);
    
    if (!file) {
        cerr << "Error in opening file!" << endl;
        return 1; // Exit if file fails to open
    }

    // Input data for 3 items
    cout << "Enter Details for three items\n";
    for (int i = 0; i < 3; i++) {
        item[i].readdata();
        file.write((char*)&item[i], sizeof(item[i]));
    }

    // Reset file pointer to the beginning for reading
    file.seekg(0);

    // Output data from the file
    cout << "\nOUTPUT\n\n";
    for (int i = 0; i < 3; i++) {
        file.read((char*)&item[i], sizeof(item[i]));
        item[i].writedata();
    }

    file.close();
    return 0;
}
