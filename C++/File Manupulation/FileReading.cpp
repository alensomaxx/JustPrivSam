/*Write a program that reads a text file and creat another file that  is identical except that every 
sequence of consecutive blank spaces is replaced by a single space*/


#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream inputFile("input.txt"); // Replace "input.txt" with your input file name
    ofstream outputFile("output.txt"); // Replace "output.txt" with your output file name

    char ch;
    bool prevSpace = false;

    while (inputFile.get(ch)) {
        if (ch == ' ' && prevSpace) {
            continue; // Skip consecutive spaces
        }

        outputFile.put(ch);
        prevSpace = (ch == ' ');
    }

    inputFile.close();
    outputFile.close();

    cout << "File processed successfully." << endl;

    return 0;
}