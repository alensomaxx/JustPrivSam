/*Manish needs a Counter class to track player scores in a game. The class should use a default constructor to initialize the score to 0, provide a method to set an initial score, increment the score, and return the current score. Ensure that after creating an instance with the default constructor, the initial value can be set and verified.

Input format :
The first line of input consists of an integer, N representing the initial value for the counter.

The second line of input consists of an integer 'random' that increments N.

Output format :
The first line of output prints the initial value.

The second line of output prints the incremented value.



Refer to the sample output for formatting specifications.

Code constraints :
-107 ≤ N, random integer ≤ 107

Sample test cases :
Input 1 :
1
100
Output 1 :
1
101
Input 2 :
-5070
777
Output 2 :
-5070
-4293*/

#include <iostream>
using namespace std;

class Counter {
private:
    int score;

public:
    // Default constructor initializing score to 0
    Counter() : score(0) {}

    // Method to set the initial score
    void setInitialScore(int initialValue) {
        score = initialValue;
    }

    // Method to increment the score by a given value
    void incrementScore(int incrementValue) {
        score += incrementValue;
    }

    // Method to return the current score
    int getScore() {
        return score;
    }
};

int main() {
    int initial, random;

    // Input for initial score and increment value
    cin >> initial;
    cin >> random;

    // Create an instance of Counter
    Counter counter;

    // Set the initial score
    counter.setInitialScore(initial);

    // Output the initial score
    cout << counter.getScore() << endl;

    // Increment the score
    counter.incrementScore(random);

    // Output the incremented score
    cout << counter.getScore() << endl;

    return 0;
}
