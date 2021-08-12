description = '''
Heap:
    - Insert -> O(log n)
    - Extract min -> O(log n)
    - heapify -> Batch insert -> O(n)
    
Heap:
    - Heap is a binary complete tree
    - at every node X_i the key of the object stored as X_i must not be greater than keys of X_i children
    - Heap is implemented as an array, where parent[arr[i]] = arr[floor(i/2)]
    - Insert:
        - Since the tree is complete, we can insert only at the end of array or in binary tree in the last level
        - Insertion can be constant time, if insertion does not violate heap property
        - 
'''


class HeapImpl:
    def __init__(self):
        self.heap_array = [None]

    def insert(self, element):
        self.heap_array.append(element)
        position = len(self.heap_array) - 1
        parent_position = self.getParent(position)
        while self.heap_array[parent_position] and self.heap_array[parent_position] > element:
            parent_elemet = self.heap_array[parent_position]

            self.heap_array[parent_position] = element
            self.heap_array[position] = parent_elemet

            position = parent_position
            parent_position = self.getParent(position)

    def getParent(self, position):
        return position // 2

    def getLeftChild(self, position):
        return position * 2

    def getRightChild(self, position):
        return 2 * position + 1

    def extraxt_min(self):
        element_at_top = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array.pop()

        position = 1
        node = self.heap_array[position]

        while True:
            leftChildPosition = self.getLeftChild(position)
            rightChildPosition = self.getRightChild(position)

            leftChild = float("inf")
            rightChild = float("inf")

            if leftChildPosition < len(self.heap_array):
                leftChild = self.heap_array[leftChildPosition]

            if rightChildPosition < len(self.heap_array):
                rightChild = self.heap_array[rightChildPosition]

            if leftChild < rightChild:
                minChildPosition = leftChildPosition
            else:
                minChildPosition = rightChildPosition

            minChild = float("inf") if minChildPosition >= len(self.heap_array) else self.heap_array[minChildPosition]

            if node < minChild:
                break
            else:
                self.heap_array[position] = minChild
                self.heap_array[minChildPosition] = node
                position = minChildPosition

        return element_at_top


if __name__ == '__main__':
    so = HeapImpl()
    for x in [4, 4, 8, 9, 4, 12, 9, 11, 13]:
        so.insert(x)
    out = so.extraxt_min()
    print(out)
    so.insert(0)
    print(so.heap_array)
