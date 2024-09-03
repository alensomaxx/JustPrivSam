#include <iostream>
using namespace std;

class ArrayOperations {
private:
    int *arr;
    int size;
    int capacity;

public:
    // Constructor to initialize the array with a given capacity
    ArrayOperations(int cap) {
        capacity = cap;
        arr = new int[capacity];
        size = 0;
    }

    // Destructor to free the allocated memory
    ~ArrayOperations() {
        delete[] arr;
    }

    // Function to insert an element into the array
    void insert(int element) {
        if (size == capacity) {
            cout << "Array is full, cannot insert new element." << endl;
            return;
        }
        arr[size] = element;
        size++;
        cout << "Element inserted successfully!" << endl;
    }

    // Function to delete an element from the array
    void deleteElement(int element) {
        int index = search(element);
        if (index == -1) {
            cout << "Element not found!" << endl;
            return;
        }
        for (int i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        size--;
        cout << "Element deleted successfully!" << endl;
    }

    // Function to search for an element in the array
    int search(int element) {
        for (int i = 0; i < size; i++) {
            if (arr[i] == element) {
                return i;
            }
        }
        return -1;
    }

    // Function to display the elements of the array
    void display() {
        if (size == 0) {
            cout << "Array is empty!" << endl;
            return;
        }
        cout << "Array elements: ";
        for (int i = 0; i < size; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    int capacity;
    cout << "Enter the capacity of the array: ";
    cin >> capacity;

    ArrayOperations array(capacity);

    int choice, element;
    do {
        cout << "\nMenu:\n";
        cout << "1. Insert element\n";
        cout << "2. Delete element\n";
        cout << "3. Search element\n";
        cout << "4. Display elements\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter the element to insert: ";
            cin >> element;
            array.insert(element);
            array.display();
            break;

        case 2:
            cout << "Enter the element to delete: ";
            cin >> element;
            array.deleteElement(element);
            array.display();
            break;

        case 3:
            cout << "Enter the element to search: ";
            cin >> element;
            int index;
            index = array.search(element);
            if (index == -1) {
                cout << "Element not found!" << endl;
            } else {
                cout << "Element found at index: " << index << endl;
            }
            break;

        case 4:
            array.display();
            break;

        case 5:
            cout << "Exiting..." << endl;
            break;

        default:
            cout << "Invalid choice! Please try again." << endl;
        }
    } while (choice != 5);

    return 0;
}