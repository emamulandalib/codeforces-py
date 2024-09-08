class Fifo:
    data = []
    limit = 0

    def __init__(self, limit):
        self.limit = limit

    def enqueue(self, data):
        if self.is_full():
            raise Exception('Fifo is full')

        self.data.append(data)

    def dequeue(self):
        if self.is_empty():
          raise Exception('Fifo is empty')

        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return len(self.data) == self.limit

    def peek(self):
        pass
