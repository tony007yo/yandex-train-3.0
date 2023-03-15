import operator

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

test_data = input().split()
operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
    }
stack = Stack()

def calculate_postfix(str):
    for s in str:
        if s not in operators:
            stack.push(int(s))
        else:
            oper2 = stack.pop()
            oper1 = stack.pop()
            stack.push(operators[s](oper1,oper2))
    print(stack.back())

calculate_postfix(test_data)