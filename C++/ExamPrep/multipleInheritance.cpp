#include <iostream>
#include <string>

using namespace std;

class Person {
public:
    string name;
    int age;
};
class Student : public Person {
public:
    int rollNo;
};
class GradStudent: public Student {
public:
    string ResearchArea;
};


int main(){
    GradStudent s1;
    s1.name="Tony Stark";
    s1.ResearchArea="AI";
    cout<<s1.name<<endl;;
    cout<<s1.ResearchArea<<endl;;


    return 0;
}