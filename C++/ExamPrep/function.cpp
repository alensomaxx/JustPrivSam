#include <iostream>
#include <string>
using namespace std;

class Teacher{
private:
    double password;
    
public:
    string name;
    string subject;
    string dept;
    double salary;

    void changeDept(string newDept){
        dept = newDept;
    }

};

int main(){




    return 0;
}