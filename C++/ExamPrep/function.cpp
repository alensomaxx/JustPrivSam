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
    Teacher t1;
    t1.name="Alen";
    t1.dept="CS";
    t1.subject="Automation";

    t1.changeDept("Maths");
    cout<<t1.name<<endl;
    cout<<t1.dept<<endl;
    cout<<t1.subject<<endl;


    return 0;
}