class Node:
    def __init__(self, value):
        self.value = value
        self.child = []

    def add(self, child):
        self.child.append(child)

    def __iter__(self):
        return iter(self.child)
    def __repr__(self):
        return "Node({!r}) ".format(self.value)

    def depth_first(self):
        yield self
        for child in self:
            yield  child.depth_first()

if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child1.add(Node(3))
    child2.add(Node(4))
    child2.add(Node(5))
    root.add(child1)
    root.add(child2)

    for c in root.depth_first():
        print(c,end='')
        
