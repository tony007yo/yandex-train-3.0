from collections import deque
import heapq

class MaxHeap():
    def __init__(self) -> None:
        self.heap = []
        self.heap_output = []

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2 

        if l < n and self.heap[i] < self.heap[l]:
            largest = l

        if r < n and self.heap[largest] < self.heap[r]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(n, largest)

    def insert(self, num):
        size = len(self.heap)
        if size == 0:
            self.heap.append(-num)
        else:
            self.heap.append(-num)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)

    def extract(self):
        size = len(self.heap)
        i = 0
            
        self.heap[i], self.heap[size - 1] = self.heap[size - 1], self.heap[i]

        res = -self.heap.pop(i)
        self.heap_output.append(f"{res}\n")
        
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify(len(self.heap), i)

        return res

if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        commands = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    commmands_len = int(commands.popleft())
    heap = MaxHeap()
    while len(commands) > 0:
        commmand = commands.popleft().split()
        if commmand[0] == "1":
            heap.extract()
        else:
            heap.insert(int(commmand[1]))

    with open('output.txt', 'w') as f_out:
        f_out.writelines(heap.heap_output)