class Queue():
    "Queue class  fist in first out"
    def __init__(self, quantum, priority):
        self.items = []
        self.quantum = quantum
        self.priority = priority

    def isEmpty(self):
        return self.items == []

    def append(self, item):
        item.quantumTime = self.quantum
        item.priority = self.priority
        self.items.insert(0,item)

    def getFirst(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
