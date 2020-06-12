class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.to_be_popped = 0   # Keeps track of the oldest index

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        else:
            self.list.pop(self.to_be_popped)
            self.list.insert(self.to_be_popped, item)

            if self.to_be_popped == self.capacity - 1:
                self.to_be_popped = 0
            else:
                self.to_be_popped += 1

    def get(self):
        return self.list