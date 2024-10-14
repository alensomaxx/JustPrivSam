#include <iostream>
using namespace std;

class B {
    int a;  
public:
    int b;  
    void get_ab(); 
    int get_a(void); 
    void show_a(void); 
};

class D : private B {  
public:
    int c;
    void mul(void);  
    void display(void); 

    // Provide public access to B's public members through D
    void set_ab() {  
        get_ab();  // now accessible from within D
    }
    
    void set_b(int value) {  // provide setter for b
        b = value;  // since b is inherited privately, we need a public method in D to access it
    }

    void show_a() {  
        B::show_a();
    }
};

void B::get_ab(void) {
    a = 5;  
    b = 10;  
}

int B::get_a() {
    return a;  // getter for private member a
}

void B::show_a() {
    cout << "a = " << a << "\n";  
}

void D::mul() {
    c = b * get_a();  
}

void D::display() {
    cout << "a = " << get_a() << "\n";  // access a through get_a()
    cout << "b = " << b << "\n";  
    cout << "c = " << c << "\n";  
}

int main() {
    D d;

    d.set_ab();   // Indirectly call B::get_ab() through a public method in D
    d.mul();
    d.show_a();   // accessed through public wrapper in D)
    d.display();  

    d.set_b(20);  // Set value of 'b' through a public setter in D
    d.mul();      
    d.display();  

    return 0;
}
