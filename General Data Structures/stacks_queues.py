'''
List of actionables for "list data structure"

list.append(x)
list.extend(iterable)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.clear()
list.index(x[, start[. end]])
list.count(x)
list.sort(key=None, reverse=False)
list.reverse()
list.copy()
list[i]
'''

# Stack is LIFO
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    # Retrieve the first element of the stack
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(4)
s.push('dog')

# Queue is FIFO
class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        return len(self.queue)

    def print_queue(self):
        for i in len(self.queue):
            print (self.queue[i])

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No element in the queue")

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())
