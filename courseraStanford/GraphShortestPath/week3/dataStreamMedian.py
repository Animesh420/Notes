from heapq import heappush, heappop, heapify


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))

        if len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # if len(self.min_heap) != len(self.max_heap):
        #     return -self.max_heap[0]
        # else:
        #     return 0.5 * (self.min_heap[0] - self.max_heap[0])
        return -self.max_heap[0]


if __name__ == '__main__':
    so = MedianFinder()
    s = 0
    count = 0
    with open("./Median.txt") as f:
        for line in f:
            count += 1
            num = int(line.rstrip())
            so.addNum(num)
            s += so.findMedian()

    print(count, s % 10000)
