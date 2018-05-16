"""iterative Deepening depth first search:
    this algroithm is processing the node the all nodes are connected to it.
    it is like waving over a graph """

def iddfs(G, s):
    yielded = set()

    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0:
            return
        if S is None:
            S = set()
        S.add(s)
        for u in G[s]:
            if u in S:
                continue
            #for v in recurse(G, u, d-1,S):
                #yield v
            yield from recurse(G, u, d-1,S)
    n = len(G)
    for d in range(n):
        if len(yielded) == n:
            break
        #for u in recurse(G, s, d):
            #yield u
        yield from recurse(G, s, d)
            
g ={'a':['b','c'], 'c':['a','b','f'], 'b':['a','c','d','e'],'f':['c','e'],
    'd':['b'],'e':['b','f']}
