"""
Binary Min Heap 

            10
          /    \
        15      30
       /  \    /   \
    40    50  100   40

Root Node ----> Arr[0]
Parent Node ---> Arr[(i-1)/2]
Left Child Node ---> Arr[(2*i)+1]
Right Child Node ---> Arr[(2*i)+2]

Operations on Min Heap:
getMin(): returns root. in O(1)
extractMin(): Removes the minimum elemen in O(Logn)
decreaseKey(): 
insert()
delete()

"""

from heapq import heappop, heappush, heapify


class MinHeap:

    # constructor to initialize a heap
    def __init__(self, *args, **kwargs):
        self.heap = []

    def parent(self, i):
        return (i-1)//2
    
    # Insert a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)
    
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val

        while i != 0 and self.heap[self.parent(i)] > self.heap[i] :
            print("before swap parent is {0} and child is {1}".format(self.heap[self.parent(i)], self.heap[i]))
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            print("after swap parent is {0} and child is {1}".format(self.heap[self.parent(i)], self.heap[i]))
            i = self.parent(i)
            print("current parent index i is ", i)

    # Remove the minimum element from the heap
    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        index = self.heap.index(i)
        print("{0} is going to be deleted in index {1}".format(i, index))
        self.decreaseKey(index, float('-inf'))
        x = self.extractMin()
        print("removed min ", x)

    def getMin(self):
        return self.heap[0]

heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)
heapObj.deleteKey(3)

print("Root is: ", heapObj.getMin())