/*Consider a class network of  figure. The class master derives information from 
both accounts and admin classes which in turn derive information from the class person. 
Define all the four classes and write a program to create, update and display the 
informination contained in objects

*/

#include <iostream>
#include <string>

using namespace std;

class Person {
protected:
    string name;
    int code;

public:
    Person(string n, int c) : name(n), code(c) {}

    virtual void setName(string n) {
        name = n;
    }

    virtual void setCode(int c) {
        code = c;
    }

    virtual string getName() const {
        return name;
    }

    virtual int getCode() const {
        return code;
    }
};

class Accounts : virtual public Person {
protected:
    int pay;

public:
    Accounts(string n, int c, int p) : Person(n, c), pay(p) {}

    void setPay(int p) {
        pay = p;
    }

    int getPay() const {
        return pay;
    }
};

class Admin : virtual public Person {
protected:
    int experience;

public:
    Admin(string n, int c, int e) : Person(n, c), experience(e) {}

    void setExperience(int e) {
        experience = e;
    }

    int getExperience() const {
        return experience;
    }
};

class Master : public Accounts, public Admin {
public:
    Master(string n, int c, int p, int e) : Accounts(n, c, p), Admin(n, c, e), Person(n, c) {}

    void displayInfo() const {
        cout << "Name: " << getName() << endl;
        cout << "Code: " << getCode() << endl;
        cout << "Pay: " << getPay() << endl;
        cout << "Experience: " << getExperience() << endl;
    }
};

int main() {
    Master m("John Doe", 123, 50000, 5);

    m.displayInfo();

    // Update information
    m.setName("Jane Smith");
    m.setPay(60000);
    m.setExperience(7);

    m.displayInfo();

    return 0;
}