class Stack:
    stack = list()

    def push(self, n):
        self.stack.append(n)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return (-1, -1)
        
    def back(self):
        if not self.is_empty():
            return self.stack[-1]
        return (-1, -1)

    def is_empty(self):
        return len(self.stack) == 0

moving_cities = Stack()

def is_correct(cities_len, cities):
    res = ["-1" for _ in range(cities_len)]
    for i in range(cities_len):
        while moving_cities.back()[1] > cities[i]:
            j, _ = moving_cities.pop()
            res[j] = str(i)
        moving_cities.push((i, cities[i]))
    print(' '.join(res))


cities_len = int(input())
brackets = is_correct(cities_len, list(map(int, input().split())))