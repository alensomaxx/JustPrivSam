/*Bindu is working on a program to convert decimal numbers to binary representation using a stack data structure implemented with a linked list. She needs your help in designing and implementing this program.



Your task is to design and implement the stack with the specified push and pop operations to support this conversion.

Input format :
The input consists of an integer d, representing the decimal number to be converted into binary.

Output format :
The output prints "Binary representation: " followed by the binary representation of the input decimal number.



Refer to the sample output for formatting specifications.

Code constraints :
The stack used for the conversion can have a maximum size of 32.

1 ≤ d ≤ 512

Sample test cases :
Input 1 :
10
Output 1 :
Binary representation: 1010
Input 2 :
37
Output 2 :
Binary representation: 100101
*/

#include <iostream>
using namespace std;

#define MAX_SIZE 32

struct Stack{
    int arr[MAX_SIZE];
    int top;
};


void initStack(Stack& stack){
    stack.top = -1;
}


bool isFull(Stack& stack){
    return stack.top == MAX_SIZE - 1;
}

bool isEmpty(Stack& stack){
    return stack.top == -1;
}

void push(Stack& stack, int element){
    if(!isFull(stack)){
        stack.arr[++stack.top]=element;
    }
}

int pop(Stack& stack){
    if(!isEmpty(stack)){
        return stack.arr[stack.top--];
    }else{
        cout<<"Stack is empty!"<<endl;
        return -1;
    }
}

void toBinar(int decimal){
    Stack stack;
    initStack(stack);
    
    if(decimal == 0){
        cout << "Binar Representation: 0"<<endl;
        return;
    }
    
    while (decimal >0){
        int remainder = decimal%2;
        push(stack,remainder);
        decimal /= 2;
    }
    
    cout << "Binary representation: ";
    while(!isEmpty(stack)){
        cout << pop(stack);
    }
    cout << endl;
}

int main(){
    int inn;
    cout<<"Enter the number which needs to be converted: ";
    cin>>inn;
    
    toBinar(inn);
 
 return 0;   
}
        
    
    