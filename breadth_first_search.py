"""breadth first search is a path that will have path from each node to all
   nodes in the graph"""
from collections import deque
class Breadth:
    """build breadth first search instance """
    def __init__(self, graph, start):
        self.__root = start
        self.__graph = graph
        self.__path = self.__build(graph, start)

    def __build(self, graph, start):

        path = {}
        path[start] = None
        queue = deque([start])
        while queue:
            vertex = queue.popleft()

            for new_vertex in graph[vertex]:
                if new_vertex in path:
                    continue
                path[new_vertex] = vertex
                queue.append(new_vertex)
        return path
    def show(self):
        return self.__path

    def pathTo(self,vertex):
        
        p = self.__path
        path = []
        while p[vertex] is not None:
            path.append(self.__graph[p[vertex]][vertex])
            vertex = p[vertex]
        path.reverse()
        return path

    def pathToEach(self):
        record = {}
        for vertex in self.__graph:
            path = self.pathTo(vertex)
            record[vertex] = len(path)
            print("pass from %s to %s: "%(self.__root, vertex),end="")
            print(path)
        print("*** from %s to all ***"%(self.__root),record)
        return record
        
            
            
        
        
        
