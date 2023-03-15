class Stack:
    stack = list()
    stack_output = list()

    def push(self, n):
        self.stack.append(int(n))
        self.stack_output.append("ok")

    def pop(self):
        if len(self.stack) > 0:
            self.stack_output.append(str(self.stack.pop()))
            return
        self.stack_output.append("error")

    def back(self):
        if len(self.stack) > 0:
            self.stack_output.append(str(self.stack[-1]))
            return
        self.stack_output.append("error")

    def size(self):
        self.stack_output.append(str(len(self.stack)))

    def clear(self):
        self.stack.clear()
        self.stack_output.append("ok")

    def exit(self):
        self.stack_output.append("bye")
        print("\n".join(self.stack_output))


if __name__ == '__main__':
    command = list(input().split())
    stack = Stack()
    i = 1
    while command[0] != "exit":
        func = getattr(stack, command[0])
        if command[0] == "push":
            func(command[1])
        else:
            func()
        command = list(input().split())
        i += 1
    getattr(stack, command[0])()