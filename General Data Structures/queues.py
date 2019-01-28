class Queue:
    def __init__(self):
        self.queue = list()

    def add_to_queue(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        return len(self.queue)

    def print_queue(self):
        for i in len(self.queue):
            print (self.queue.value)

# List of actionables for "list data structure"
# list.append(x)
# list.extend(iterable)
# list.insert(i, x)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[, start[. end]])
# list.count(x)
# list.sort(key=None, reverse=False)
# list.reverse()
# list.copy()
