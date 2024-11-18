#include <iostream>
using namespace std;

void divide(int x, int y, int z)
{
    cout<<"\n We are inside the function \n";
    if ((x-y) != 0)
    {
        int R = z/(x-y);
        cout<<"Result = "<< R << "\n";
    }
    else
    {
        throw(x-y);
    }
}
int main(){
    try
    {
        {cout << "We are inside the try block \n";
        divide(10,20,30);
        divide(10,10,20);
        }
    }
    catch(int i)
    {
        cout<<"Caught the exception \n";
    }
    return 0;
}