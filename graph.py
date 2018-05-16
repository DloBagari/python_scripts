from Heap import Heap
class Node:
    "node to represent vetice in the graph"
    def __init__(self,name):
        self.__name = name
        self.__links = []
        self.__visited = False
        self.__from = None
        self.__cost = 0

    def __eq__(self, other):
        return self.getName() == other.getName()

    def addLinks(self, *link):
        self.__links.extend(list(link))

    def getName(self):
        return self.__name

    def links(self):
        return self.__links

    def visited(self):
        return self.__visited

    def setVisit(self):
        self.__visited = True

    def setFrom(self,node):
        self.__from = node

    def fromNode(self):
        return self.__from

    def getCost(self):
        return self.__cost

    def setCost(self, cost):
        self.__cost = cost

    def travese(self):
        print(self.getName())
        self.__visited = True
        for link in self.links():
            if not link.toNode().visited():
                link.toNode().travese()
    def __str__(self):
        return self.__name


class Link:
    "a link between two nodes"
    def __init__(self, weight,to,fro):
        self.__weight = weight
        self.__to= to
        self.__from = fro

    def getWeight(self):
        return self.__weight

    def toNode(self):
        return self.__to

    def getFrom(self):
        return self.__from


class Spanning:
    "create the miminal spanning tree"
    def __init__(self, root,ln):
        self.__root = root
        self.__seen = []
        self.__links = Heap()
        self.__shorts = []
        self.__length = ln

    def walk(self,to=None):
        if to is None:
            self.__walkToEnd()
        else:
            self.__walkTo(to)

    def __walkToEnd(self):
        while len(self.__seen) < self.__length:
            self.__root.setVisit()
            self.__seen.append(self.__root)
            print(self.tree())
            self.__findLinks(self.__root)
            if len(self.__seen) == self.__length:
                break
            less = self.getnext()
            self.__shorts.append(less)
            self.__root = less.toNode()

    def __walkTo(self, to):
        while self.__root.getName() != to:
            self.__root.setVisit()
            self.__seen.append(self.__root)
            print(self.tree())
            self.__findLinks(self.__root)
            if self.__root.getName() == to:
                break
            less = self.getnext()
            self.__shorts.append(less)
            self.__root = less.toNode()

    def getnext(self):
        less = less = self.__links.mini()
        while less.toNode().visited():
            less = less = self.__links.mini()
        less.toNode().setFrom(less.getFrom())
        less.toNode().setCost(less.getFrom().getCost()+less.getWeight())
        return less
        
            

    def __findLinks(self, node):
        print(node,"finding")
        for link in node.links():
            if not link.toNode().visited():
                self.__links.add(link)
    def tree(self):
        return [i.getName() for i in self.__seen]

    def result(self):
        print( [(i.getFrom().getName(), i.toNode().getName(),i.getWeight()) \
                for i in self.__shorts])

    def path(self):
        result = ""
        node = self.__shorts[-1].toNode()
        cost =node.getCost()
        print(node.fromNode())
        while node.fromNode() is not None:
            result = "-->"+node.getName() + result
            node = node.fromNode()
        return node.getName() + result +" = " + str(cost)
            
    
    def dd(self):
        for node in self.__seen:
            print(node.fromNode())
        
        

if __name__ == "__main__":
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    H = Node("H")
    L = Node("L")
    A.addLinks(Link(3,B,A), Link(2,E,A), Link(5,D,A))
    B.addLinks(Link(3,A,B), Link(6,C,B))
    C.addLinks(Link(6,B,C), Link(9,D,C), Link(3,H,C),Link(1,F,C))
    D.addLinks(Link(5,A,D), Link(3,E,D), Link(4,L,D), Link(9,C,D))
    E.addLinks(Link(2,A,E), Link(5,L,E), Link(3,D,E))
    L.addLinks(Link(5,E,L), Link(4,D,L), Link(7,F,L))
    F.addLinks(Link(7,L,F), Link(2,H,F), Link(1,C,F))
    H.addLinks(Link(2,F,H), Link(3,C,H))
    sp = Spanning(A,8)
    sp.walk("F")
    sp.result()
    print(sp.path())
  
    

"""seen = []
    q = [A]
    while q:
        node = q.pop()
        if node not in seen:
            seen.add(node)
            print(node.getName())
            node.setVisit()
            for link in node.links():
                if not link.toNode().visited():
                    q.append(link.toNode())""" 
                
    
                
                
    
        
