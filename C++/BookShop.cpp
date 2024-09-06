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
    Books(const char* a, const char* t, const char* p, float pr, int s) {
        author = new char[strlen(a) + 1];
        strcpy(author, a);

        title = new char[strlen(t) + 1];
        strcpy(title, t);

        publisher = new char[strlen(p) + 1];
        strcpy(publisher, p);

        price = pr;
        stock = s;
    }

    // Destructor to free dynamically allocated memory
    ~Books() {
        delete[] author;
        delete[] title;
        delete[] publisher;
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

int main() {
    // Creating an array of books with dynamic memory allocation
    Books book1("J.K. Rowling", "Harry Potter", "Bloomsbury", 39.99, 50);
    Books book2("George Orwell", "1984", "Secker & Warburg", 19.99, 30);
    
    // Input from the customer
    char searchTitle[50], searchAuthor[50];
    cout << "Enter the title of the book: ";
    cin.getline(searchTitle, 50);
    cout << "Enter the author of the book: ";
    cin.getline(searchAuthor, 50);
    
    // Searching and selling books
    if (book1.searchBook(searchTitle, searchAuthor)) {
        book1.showDetails();
        int copies;
        cout << "Enter number of copies required: ";
        cin >> copies;
        book1.sellBook(copies);
    } else if (book2.searchBook(searchTitle, searchAuthor)) {
        book2.showDetails();
        int copies;
        cout << "Enter number of copies required: ";
        cin >> copies;
        book2.sellBook(copies);
    } else {
        cout << "Book not available" << endl;
    }
    
    return 0;
}


