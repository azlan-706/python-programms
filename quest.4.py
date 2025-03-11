import heapq

class MedianHeap:
    def __init__(self):
        self.low = []  # Max-Heap (negative values stored)
        self.high = []  # Min-Heap

    def insert(self, x):
        """Insert a number while maintaining balance."""
        if not self.low or x <= -self.low[0]:  # Insert into max-heap
            heapq.heappush(self.low, -x)
        else:  # Insert into min-heap
            heapq.heappush(self.high, x)

        self._balance_heaps()

    def delete(self, x):
        """Delete a number and rebalance."""
        if self.low and x <= -self.low[0]:  # Check if in max-heap
            self._remove_from_heap(self.low, -x)
        elif self.high and x >= self.high[0]:  # Check if in min-heap
            self._remove_from_heap(self.high, x)
        
        self._balance_heaps()

    def findMedian(self):
        """Find median of the current numbers."""
        if len(self.low) > len(self.high):
            return -self.low[0]
        elif len(self.high) > len(self.low):
            return self.high[0]
        return (-self.low[0] + self.high[0]) / 2

    def _balance_heaps(self):
        """Ensure both heaps have balanced sizes."""
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def _remove_from_heap(self, heap, value):
        """Remove a specific value from a heap."""
        index = heap.index(value)  # Find the index
        heap[index] = heap[-1]  # Replace with last element
        heap.pop()
        if index < len(heap):
            heapq.heapify(heap)  # Restore heap property

# Example Usage
medianHeap = MedianHeap()
medianHeap.insert(10)
medianHeap.insert(20)
medianHeap.insert(15)
print(medianHeap.findMedian())  # 15
medianHeap.delete(15)
print(medianHeap.findMedian())  # (10+20)/2 = 15
medianHeap.insert(5)
print(medianHeap.findMedian())  # 10
