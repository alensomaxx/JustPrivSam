/* You will perform the following operations:
1.	Traversal: Go through the list of inventory quantities to verify the stock levels.
2.	Insertion: Add a new item to the inventory, updating the quantity.
3.	Deletion: Remove an item from the inventory when it is out of stock.
Input format :
The first line of input contains an integer x, representing the number of items in the inventory.
The second line contains x space-separated integers, each representing the quantity of an item in the inventory.
The third line contains an integer n, representing the number of items to be newly added.
The fourth line contains n space-separated integers, each representing the quantity of a new item to be added to the inventory.
The fifth line contains an integer m, representing the number of items to be removed.
The sixth line contains m space-separated integers, each representing the quantity of an item to be removed from the inventory.
Output format :
The
 first line of output prints "Inventory List: " followed by the 
quantities of the items in the inventory, separated by spaces.
After each insertion:

Print "Inserting Item: " followed by the quantity of the new item being added.
Print "Inventory List: " followed by the updated inventory quantities, separated by spaces.
After each deletion:

Print "Removing Item: " followed by the quantity of the item being removed.
Print "Inventory List: " followed by the updated inventory quantities, separated by spaces.

Refer to the sample output for formatting specifications.
Code constraints :
The given test cases fall under the following constraints:
1 ≤ x ≤ 10
1 ≤ n, m ≤ 5
Sample test cases :
Input 1 :

3
50 120 30
2
75 200
2
120 50
Output 1 :

Inventory List: 50 120 30 
Inserting Item: 75
Inventory List: 50 120 30 75 
Inserting Item: 200
Inventory List: 50 120 30 75 200 
Removing Item: 120
Inventory List: 50 30 75 200 
Removing Item: 50
Inventory List: 30 75 200 
Input 2 :

4
12 78 35 69
1
42
3
42 35 69
Output 2 :

Inventory List: 12 78 35 69 
Inserting Item: 42
Inventory List: 12 78 35 69 42 
Removing Item: 42
Inventory List: 12 78 35 69 
Removing Item: 35
Inventory List: 12 78 69 
Removing Item: 69
Inventory List: 12 78 */

#include <iostream>
#include <vector>

using namespace std;

void insertItem(vector<int>& inventory, int quantity) {
    inventory.push_back(quantity);
    cout << "Inserting Item: " << quantity << endl;
}

void removeItem(vector<int>& inventory, int quantity) {
    for (int i = 0; i < inventory.size(); i++) {
        if (inventory[i] == quantity) {
            inventory.erase(inventory.begin() + i);
            cout << "Removing Item: " << quantity << endl;
            return;
        }
    }
    cout << "Item not found." << endl;
}

int main() {
    int x, n, m;

    cin >> x;
    vector<int> inventory(x);
    for (int i = 0; i < x; i++) {
        cin >> inventory[i];
    }

    cout << "Inventory List: ";
    for (int quantity : inventory) {
        cout << quantity << " ";
    }
    cout << endl;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int quantity;
        cin >> quantity;
        insertItem(inventory, quantity);
    }

    cin >> m;
    for (int i = 0; i < m; i++) {
        int quantity;
        cin >> quantity;
        removeItem(inventory, quantity);
    }

    cout << "Inventory List: ";
    for (int quantity : inventory) {
        cout << quantity << " ";
    }
    cout << endl;

    return 0;
}

