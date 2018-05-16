def dfs(graph, start, discovered=None, finished=None, seen=None, time = 0):
    """deep first search ,with timestep for discovering the node and finishing
       process on the node"""
    if discovered == finished == seen:
        discovered = {}
        finished = {}
        seen = set()
    discovered[start]= time
    time += 1
    seen.add(start)
    for vertex in graph[start]:
        if vertex in seen:
            continue
        time = dfs(graph, vertex,discovered, finished, seen, time)
    finished[start] = time
    time +=1
    print(discovered,finished)
    return time

def dfs_topologicalSort(graph):
    """deep first search ,with timestep and return a sorted list of
       node topological( nearet for farest)"""
    seen = set()
    result = []

    def rec(u):
        if u in seen:
            return
        seen.add(u)
        for v in graph[u]:
            rec(v)
        result.append(u)

    for u in graph:
        rec(u)
    result.reverse()
    return result
    
            
        
    
