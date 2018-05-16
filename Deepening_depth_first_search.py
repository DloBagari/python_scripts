"""iterative Deepening depth first search:
    this algroithm is processing the node the all nodes are connected to it.
    it is like waving over a graph """

class DeepeningDepth:
    "visit each node then visit its subnodes"
    def __init__(self): 
        self.__yielded = None
        self.__graph = None
        self.__start = None 

    def __call__(self, graph, start ):
        self.__graph = graph
        self.__start = start
        # we have to set yielded to empty set ,which will empties yiled on each call
        self.__yielded = set()
        number_nodes = len(self.__graph)
        for deep in range(number_nodes):
            if len(self.__yielded) == number_nodes:
                break
            yield from self.deepTo(self.__graph,self.__start, deep)

    def deepTo(self, graph, start, deep, seen=None):
        if start not in self.__yielded:
            yield start
            self.__yielded.add(start)
        if seen is None:
            seen = set()
        seen.add(start)
        if deep == 0:
            return
        for new_node in self.__graph[start]:
            if new_node in seen:
                continue
            yield from self.deepTo(graph, new_node, deep-1, seen)
