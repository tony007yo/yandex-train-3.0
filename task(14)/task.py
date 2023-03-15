class Stack:
    stack = list()

    def push(self, n):
        self.stack.append(n)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
        
    def back(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

dead_end = Stack()

def is_correct(train_len, train):
    min_value = 1
    for i in range(train_len):
        dead_end.push(train[i])
        while dead_end.back() == min_value:
            dead_end.pop()
            min_value += 1

    while not dead_end.is_empty():
        if dead_end.pop() == min_value:
            min_value += 1
        else:
            print("NO")
            return

    print("YES")


train_len = int(input())
brackets = brackets = is_correct(train_len, list(map(int, input().split())))