#include <iostream>

using namespace std;

void test(int x) {
    try {
        if (x == 1) throw x;
        else if (x == 0) throw 'x';
        else if (x == -1) throw 1.0;
        cout << "End of try-block \n";
    }
    catch (char c) {
        cout << "Caught a Character \n";
    }
    catch (int m) {
        cout << "Caught an integer \n";
    }
    catch (double d) {
        cout << "Caught a double \n";
    }
    cout << "End of try-catch system \n\n";
}

int main() {
    test(1);
    test(0);
    test(-1);
    test(2);
    test(4);
    test(0);
    test(-1);
    
    test(0);
    test(4);
    test(3);

    return 0;
}