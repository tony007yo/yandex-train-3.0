from collections import deque

class Queue:
    buf_size = 256
    is_overflow = False
    queue = [0 for _ in range(buf_size)]
    head = 0
    tail = 0

    queue_output = list()    

    def push(self, n):
        self.__trim_update()
        self.queue[self.tail] = int(n)
        self.tail += 1 
        self.queue_output.append("ok\n")

    def pop(self):
        self.__trim_update()
        if self._size() > 0:
            self.queue_output.append(f"{str(self.queue[self.head])}\n")
            self.head += 1
            return
        self.queue_output.append("error\n")

    def front(self):
        self.__trim_update()
        if self._size() > 0:
            self.queue_output.append(f"{str(self.queue[self.head])}\n")
            return
        self.queue_output.append("error\n")

    def _size(self):
        size = None

        if self.tail >= self.head:
            size = self.tail - self.head
        else:
            size = len(self.queue) + self.tail - self.head 
        
        if size == len(self.queue) - 1:
            self.is_overflow = True
            return size

        self.tail = self.tail % self.buf_size
        self.head = self.head % self.buf_size
        
        return size

    def size(self):
        self.queue_output.append(f"{str(self._size())}\n")

    def __trim_update(self):
        # for correct size all the time
        self._size()
        if self.is_overflow:
            self.buf_size *= 2

            new_queue = [0 for _ in range(self.buf_size)]
            j = 0
            if self.tail < self.head:
                for i in range(self.head, len(self.queue), 1):
                    new_queue[j] = self.queue[i]
                    j += 1
                for i in range(self.tail):
                    new_queue[j] = self.queue[i]
                    j += 1
            else:
                for i in range(self.head, self.tail, 1):
                    new_queue[j] = self.queue[i]
                    j += 1
            self.queue = new_queue

            self.head = 0
            self.tail = j
            self.is_overflow = False


    def clear(self):
        self.queue.clear()
        self.queue = [0 for _ in range(self.buf_size)]
        self.head = 0
        self.tail = 0
        self.is_overflow = False
        self.queue_output.append("ok\n")

    def exit(self):
        self.queue_output.append("bye")
        with open('output.txt', 'w') as f_out:
            f_out.writelines(self.queue_output)

if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        commands = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    command = commands.popleft().split()
    queue = Queue()
    i = 1
    while command[0] != "exit":
        func = getattr(queue, command[0])
        if command[0] == "push":
            func(command[1])
        else:
            func()
        command = list(commands.popleft().split())
        i += 1
    getattr(queue, command[0])()