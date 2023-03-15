from collections import deque

class Stack_Indexed:
    def __init__(self) -> None:
        self.stack = list()
        
    def push(self, n):
        self.stack.append(int(n))
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def get(self, i):
        if i < len(self.stack):
            return self.stack[i]
        return None

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()


class Deque:
    buf_size = 101
    deque_front = Stack_Indexed()
    deque_back = Stack_Indexed()
    front_head = 0
    back_head = 0

    deque_output = list()

    def push_front(self, n):
        self.__trim_update()
        self.deque_front.push(int(n))
        self.deque_output.append("ok\n")

    def push_back(self, n):
        self.__trim_update()
        self.deque_back.push(int(n))
        self.deque_output.append("ok\n")
    
    def pop_front(self):
        self.__trim_update()
        if self.deque_front.size() > 0:
            self.deque_output.append(f"{str(self.deque_front.pop())}\n")
            return
        elif self.deque_back.size() > 0 and self.back_head != self.deque_back.size():
            self.deque_output.append(f"{str(self.deque_back.get(self.back_head))}\n")
            self.back_head += 1
            return

        self.deque_output.append("error\n")

    def pop_back(self):
        self.__trim_update()
        if self.deque_back.size() > 0:
            self.deque_output.append(f"{str(self.deque_back.pop())}\n")
            return
        elif self.deque_front.size() > 0 and self.front_head != self.deque_front.size():
            self.deque_output.append(f"{str(self.deque_front.get(self.front_head))}\n")
            self.front_head += 1
            return

        self.deque_output.append("error\n")

    def front(self):
        self.__trim_update()
        if self.deque_front.size() > 0:
            self.deque_output.append(f"{str(self.deque_front.get(-1))}\n")
            return
        elif self.deque_back.size() > 0 and self.back_head != self.deque_back.size():
            self.deque_output.append(f"{str(self.deque_back.get(self.back_head))}\n")
            return

        self.deque_output.append("error\n")
    
    def back(self):
        self.__trim_update()
        if self.deque_back.size() > 0:
            self.deque_output.append(f"{str(self.deque_back.get(-1))}\n")
            return
        elif self.deque_front.size() > 0 and self.front_head != self.deque_front.size():
            self.deque_output.append(f"{str(self.deque_front.get(self.front_head))}\n")
            return

        self.deque_output.append("error\n")

    def _size(self):
        return self.deque_back.size() + self.deque_front.size() - self.back_head - self.front_head

    def size(self):
        self.deque_output.append(f"{str(self._size())}\n")

    def __trim_update(self):
        if self._size() == self.buf_size\
            or (self.front_head >= self.buf_size // 2 or self.back_head >= self.buf_size // 2) or self._size() == 0:
            new_deque_back = Stack_Indexed()
            new_deque_front = Stack_Indexed()

            while self.deque_front.size() > self.front_head:
                new_deque_front.push(self.deque_front.pop())

            while self.deque_back.size() > self.back_head:
                new_deque_back.push(self.deque_back.pop())

            self.deque_front = new_deque_front
            self.deque_back = new_deque_back
            
            self.front_head = 0
            self.back_head = 0


    def clear(self):
        self.deque_front.clear()
        self.deque_back.clear()
        self.front_head = 0
        self.back_head = 0
        self.deque_output.append("ok\n")

    def exit(self):
        self.deque_output.append("bye")
        with open('output.txt', 'w') as f_out:
            f_out.writelines(self.deque_output)


if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        commands = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    command = commands.popleft().split()
    deq = Deque()
    while command[0] != "exit":
        func = getattr(deq, command[0])
        if command[0] == "push_back" or command[0] == "push_front":
            func(command[1])
        else:
            func()
        command = list(commands.popleft().split())
    getattr(deq, command[0])()  