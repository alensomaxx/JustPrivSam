#include <iostream>

// Base class
class Animal {
public:
    void eat() {
        std::cout << "Animal is eating." << std::endl;
    }
};

// Derived class from Animal
class Dog : public Animal {
public:
    void bark() {
        std::cout << "Dog is barking." << std::endl;
    }
};

// Derived class from Dog
class GoldenRetriever : public Dog {
public:
    void fetch() {
        std::cout << "Golden Retriever is fetching." << std::endl;
    }
};

int main() {
    // Create objects of derived classes
    GoldenRetriever goldenRetriever;
    Dog dog;

    // Access methods from base and derived classes
    goldenRetriever.eat();
    goldenRetriever.bark();
    goldenRetriever.fetch();

    dog.eat();
    dog.bark();

    return 0;
}