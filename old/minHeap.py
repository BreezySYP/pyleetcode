import sys

class minHeap:
    'Index start from 1'
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.heap = [0] * (maxSize + 1)
        self.heap[0] = -1 * sys.maxsize
        self.FRONT = 1
        self.size = 0

    def parent(self, pos):
        return pos // 2

    def leftNode(self, pos):
        return pos * 2

    def rightNode(self, pos):
        return (pos * 2) + 1

    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, lpos, rpos):
        self.heap[lpos], self.heap[rpos] = self.heap[rpos], self.heap[lpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.heap[pos] > self.heap[self.leftNode(pos)] or 
                self.heap[pos] > self.heap[self.rightNode(pos)]):

                if self.heap[self.leftNode(pos)] < self.heap[self.rightNode(pos)]:
                    self.swap(pos, self.leftNode(pos))
                    self.minHeapify(self.leftNode(pos))
                else:
                    self.swap(pos, self.rightNode(pos))
                    self.minHeapify(self.rightNode(pos))

    def insert(self, value):
        if self.size > self.maxSize:
            return

        self.size += 1
        self.heap[self.size] = value
        currentPos = self.size
        while self.heap[currentPos] < self.heap[self.parent(currentPos)]:
            self.swap(currentPos, self.parent(currentPos))
            currentPos = self.parent(currentPos)

    def heapify(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def pop(self):
        minValue = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return minValue

    def print(self):
        for pos in range(1, self.size//2 + 1):
            print("Parent is: " + str(self.heap[pos]) + " Left child is: " + 
                str(self.heap[self.leftNode(pos)]) +" Right child is: " + 
                str(self.heap[self.rightNode(pos)]))

heap = minHeap(15)
heap.insert(2)
heap.insert(5)
heap.insert(15)
heap.insert(7)
heap.insert(8)
heap.insert(10)
heap.insert(20)
heap.insert(1)
heap.heapify()
heap.print()

print("after pop the value: " + str(heap.pop()))
heap.print()



