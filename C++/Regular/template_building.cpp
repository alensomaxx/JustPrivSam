#include <iostream>
using namespace std;

template <class T>
void swap(T &x, T &y)
{
    T temp = x;
    x=y;
    y=temp;
}
void fun(int m, int n, float a, float b)
{
    cout << "m and n before swap: "<< m << " " << n << "\n";
    swap(m,n);
    cout << "m and n after swap: "<< m << " " << n << "\n";

    cout << "a and b before swap: "<< a << " " << b << "\n";
    swap(a,b);
    cout << "a and b after swap: "<< a << " " << b << "\n";
    
}

int main()
{
    fun(100,200,11.22,33.44);
    return 0;
}