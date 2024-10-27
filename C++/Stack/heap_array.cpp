#include <iostream>

using namespace std;

class Heap {
public:
    Heap(int capacity) {
        heap = new int[capacity];
        size = 0;
        this->capacity = capacity;
    }

    ~Heap() {
        delete[] heap;
    }

    void insert(int value) {
        if (size == capacity) {
            cout << "Heap is full." << endl;
            return;
        }

        heap[size] = value;
        size++;
        heapifyUp(size - 1);
    }

    void extractMax() {
        if (size == 0) {
            cout << "Heap is empty." << endl;
            return;
        }

        swap(heap[0], heap[size - 1]);
        size--;
        heapifyDown(0);
    }

    int getMax() {
        if (size == 0) {
            cout << "Heap is empty." << endl;
            return -1; // Or any appropriate error value
        }
        return heap[0];
    }

private:
    int *heap;
    int size;
    int capacity;

    void heapifyUp(int index) {
        while (index > 0 && heap[index] > heap[(index - 1) / 2]) {
            swap(heap[index], heap[(index - 1) / 2]);
            index = (index - 1) / 2;
        }
    }

    void heapifyDown(int index) {
        int largest = index;
        int leftChild = 2 * index + 1;
        int rightChild = 2 * index + 2;

        if (leftChild < size && heap[leftChild] > heap[largest]) {
            largest = leftChild;
        }

        if (rightChild < size && heap[rightChild] > heap[largest]) {
            largest = rightChild;
        }

        if (largest != index) {
            swap(heap[index], heap[largest]);
            heapifyDown(largest);
        }
    }
};

int main() {
    Heap h(10);
    h.insert(10);
    h.insert(20);
    h.insert(30);
    h.insert(40);
    h.insert(50);
    h.insert(60);
    h.insert(99);
    h.insert(222);
    

    cout << "Maximum value: " << h.getMax() << endl;

    h.extractMax();
    cout << "Maximum value after extraction: " << h.getMax() << endl;

    return 0;
}