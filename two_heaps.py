#questions
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# solution:

import heapq
class MedianFinder():
    def __init__(self):
        self.max_heap = [] #max_heap implemented using heapq with negation
        self.min_heap = []

    def addNum(self, num:int):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        #balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # Calculate the median based on the sizes of heaps
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
        
obj = MedianFinder()
obj.addNum(5)
obj.addNum(8)
obj.addNum(2)
obj.addNum(9)
print(obj.min_heap)
print(obj.max_heap)
print(obj.findMedian())


