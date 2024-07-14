
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap) - 1)

    def get_max(self):
        return self.heap[0] if self.heap else None

    def delete(self):
        if len(self.heap) > 1:
            max_val, self.heap[0] = self.heap[0], self.heap[-1]
            self.heap.pop()
            self.__max_heapify(0)
            return max_val
        elif self.heap:
            return self.heap.pop()
        return None

    def __percolate_up(self, index):
        while index and self.heap[(index - 1) // 2] < self.heap[index]:
            self.heap[(index - 1) // 2], self.heap[index] = self.heap[index], self.heap[(index - 1) // 2]
            index = (index - 1) // 2

    def __max_heapify(self, index):
        while True:
            left, right = index * 2 + 1, index * 2 + 2
            largest = index
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print("Max value:", heap.get_max())  

print("Deleted max value:", heap.delete()) 

print("New max value:", heap.get_max())  

heap.insert(1000)
print("New max value:", heap.get_max())  

print("Deleted max value:", heap.delete()) 

print("New max value:", heap.get_max()) 