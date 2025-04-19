// Linked List is something which can relate to as a chain of data where 
// each end of the chain we will get the details of the next node

#include <iostream>
using namespace std;

int secondLargest(int arr[], int n){
    if (n<2){
        return -1;
    }

    int largest = arr[0];
    int sLargest = -1;
    for (int i=1; i<n; i++){
        if (arr[i]> largest){
            sLargest = largest;
            largest = arr[i];
        } else if (arr[i] < largest && arr[i] > sLargest){
            sLargest = arr[i];
        }

    }
    return sLargest;
}

int main(){
    int size;
    cin>>size;
    if (size<= 0){
        cout << "Invalid array size!"<< endl;
        return 1;
    }   
    int arr[100];
    for (int i=0; i<size; i++){
        cin>> arr[i];
    }

    int s_largest = secondLargest(arr, size);
    cout << "The Second Largest number is : "<< s_largest<< endl;

    return 0;
}