class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        """Insert a new value into the max-heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the maximum value from the heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        """Move the newly added element up to maintain max-heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """Move the root element down to maintain max-heap property."""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        """Insert a new value into the min-heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the minimum value from the heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
        """Move the newly added element up to maintain min-heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """Move the root element down to maintain min-heap property."""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


# Example Usage:
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(20)
max_heap.push(5)
print(max_heap.pop())  # 20
print(max_heap.pop())  # 10

min_heap = MinHeap()
min_heap.push(10)
min_heap.push(20)
min_heap.push(5)
print(min_heap.pop())  # 5
print(min_heap.pop())  # 10
