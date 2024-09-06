/* A book shop maintains the inventory of books thar are being sold at the shop.
 The list includes details such as author, titile , price, publisher and stock position. 
 Whenever a customer wants a book, the sale person inputs the title and aithor and the system 
searches the list and displays whether it is available or not. if it is not, 
an appropriate message is displayed. If it is, then the system displayes 
the books detials and request for the number of copies required. If the requested 
copies are avaialble, the total cost of he requested copies is diplayed, otherwise the message 
"Required copies not in stock" is displayed.
Design a system using a class called Books with suitable member functions and 
constructors. Use new operator in constructor.
Use new operator in constructors to allocate memory spcae required"*/

#include <iostream>
#include <cstring>
using namespace std;

class Books {
private:
    char* author;
    char* title;
    char* publisher;
    float price;
    int stock;

public:
    // Constructor to initialize book details and allocate memory using new operator
    Books() {
        author = nullptr;
        title = nullptr;
        publisher = nullptr;
        price = 0.0;
        stock = 0;
    }

    // Destructor to free dynamically allocated memory
    ~Books() {
        delete[] author;
        delete[] title;
        delete[] publisher;
    }

    // Function to input book details
    void inputBookDetails() {
        char temp[100];

        cout << "Enter Author Name: ";
        cin.ignore();
        cin.getline(temp, 100);
        author = new char[strlen(temp) + 1];
        strcpy(author, temp);

        cout << "Enter Book Title: ";
        cin.getline(temp, 100);
        title = new char[strlen(temp) + 1];
        strcpy(title, temp);

        cout << "Enter Publisher Name: ";
        cin.getline(temp, 100);
        publisher = new char[strlen(temp) + 1];
        strcpy(publisher, temp);

        cout << "Enter Price: ";
        cin >> price;

        cout << "Enter Stock: ";
        cin >> stock;
    }

    // Function to display book details
    void showDetails() const {
        cout << "Title: " << title << endl;
        cout << "Author: " << author << endl;
        cout << "Publisher: " << publisher << endl;
        cout << "Price: $" << price << endl;
        cout << "Stock: " << stock << " copies available" << endl;
    }

    // Function to check if the book matches the title and author entered by the user
    bool searchBook(const char* t, const char* a) const {
        return (strcmp(t, title) == 0 && strcmp(a, author) == 0);
    }

    // Function to sell the book if sufficient stock is available
    void sellBook(int copies) {
        if (stock >= copies) {
            float totalCost = price * copies;
            stock -= copies;
            cout << "Total cost: $" << totalCost << endl;
        } else {
            cout << "Required copies not in stock" << endl;
        }
    }
};

// Menu-driven function
void menu(Books books[], int& count) {
    int choice;
    do {
        cout << "\n--- Book Shop Menu ---" << endl;
        cout << "1. Add Book" << endl;
        cout << "2. Search and Buy Book" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                if (count < 100) {
                    books[count].inputBookDetails();
                    count++;
                    cout << "Book added successfully!" << endl;
                } else {
                    cout << "Inventory full, cannot add more books!" << endl;
                }
                break;
            }

            case 2: {
                char searchTitle[50], searchAuthor[50];
                cout << "Enter the title of the book: ";
                cin.ignore();
                cin.getline(searchTitle, 50);
                cout << "Enter the author of the book: ";
                cin.getline(searchAuthor, 50);

                bool found = false;
                for (int i = 0; i < count; i++) {
                    if (books[i].searchBook(searchTitle, searchAuthor)) {
                        books[i].showDetails();
                        int copies;
                        cout << "Enter number of copies required: ";
                        cin >> copies;
                        books[i].sellBook(copies);
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    cout << "Book not available" << endl;
                }
                break;
            }

            case 3:
                cout << "Exiting..." << endl;
                break;

            default:
                cout << "Invalid choice! Please try again." << endl;
                break;
        }
    } while (choice != 3);
}

int main() {
    Books books[100];  // Array to store up to 100 books
    int count = 0;     // To keep track of the number of books in inventory

    menu(books, count);

    return 0;
}
