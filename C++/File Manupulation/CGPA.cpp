/*Write a program to insert the data for 'n' students in a file 
read the compleete data and print the average CGPA of all students*/

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

class Student {
    char name[30];
    int rollNo;
    float cgpa;
public:
    void readdata();
    void writedata() const;
    float getCgpa() const;
};

// Function to read data for each student
void Student::readdata() {
    cout << "Enter Name: "; 
    cin >> name;
    cout << "Enter Roll No: "; 
    cin >> rollNo;
    cout << "Enter CGPA: "; 
    cin >> cgpa;
}

// Function to write student data
void Student::writedata() const {
    cout << setiosflags(ios::left)
         << setw(20) << name
         << setw(10) << rollNo
         << setw(5) << setprecision(2) << fixed << cgpa
         << endl;
}

// Function to get CGPA
float Student::getCgpa() const {
    return cgpa;
}

int main() {
    int n;
    cout << "Enter the number of students: ";
    cin >> n;

    Student* students = new Student[n];
    fstream file;

    // Open the file to write the data
    file.open("STUDENT.DAT", ios::out | ios::binary);
    if (!file) {
        cout << "Error in opening file!" << endl;
        return 1;
    }

    // Input data for 'n' students
    cout << "Enter details for " << n << " students:\n";
    for (int i = 0; i < n; i++) {
        students[i].readdata();
        file.write((char*)&students[i], sizeof(students[i]));
    }

    file.close(); // Close the file after writing

    // Open the file to read data
    file.open("STUDENT.DAT", ios::in | ios::binary);
    if (!file) {
        cout << "Error in opening file!" << endl;
        return 1;
    }

    cout << "\nSTUDENT DETAILS\n";
    cout << setw(20) << "Name" << setw(10) << "RollNo" << setw(5) << "CGPA" << endl;

    float totalCgpa = 0;
    for (int i = 0; i < n; i++) {
        file.read((char*)&students[i], sizeof(students[i]));
        students[i].writedata();
        totalCgpa += students[i].getCgpa(); // Sum the CGPA
    }

    file.close(); // Close the file after reading

    // Calculate and display the average CGPA
    float avgCgpa = totalCgpa / n;
    cout << "\nAverage CGPA: " << setprecision(2) << fixed << avgCgpa << endl;

    delete[] students; // Free the allocated memory

    return 0;
}
