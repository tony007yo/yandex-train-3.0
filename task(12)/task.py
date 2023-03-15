class Stack:
    stack = list()

    def push(self, n):
        self.stack.append(n)
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
        
    def back(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

valid_brackets = {"(":")", "{":"}", "[":"]"}
stack = Stack()

def is_correct(string):
    for bracket in string:
        if bracket in valid_brackets.keys():
            stack.push(bracket)
        elif valid_brackets.get(stack.pop()) != bracket:
            print("no")
            return
            
    if stack.size() == 0:
        print("yes")
    else:
        print("no")


brackets = is_correct(input())