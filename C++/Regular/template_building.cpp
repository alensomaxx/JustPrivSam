#include <iostream>
using namespace std;

namespace custom {  // Custom namespace to avoid conflict
    template <class T>
    void swap(T &x, T &y) {
        T temp = x;
        x = y;
        y = temp;
    }
}

void fun(int &m, int &n, float a, float b) {
    cout << "m and n before swap: " << m << " " << n << "\n";
    custom::swap(m, n);  // Call swap from the custom namespace
    cout << "m and n after swap: " << m << " " << n << "\n";

    cout << "a and b before swap: " << a << " " << b << "\n";
    custom::swap(a, b);  // Call swap from the custom namespace
    cout << "a and b after swap: " << a << " " << b << "\n";
}

int main() {
    int m = 100, n = 200;
    float a = 11.22, b = 33.44;
    fun(m, n, a, b);
    return 0;
}
