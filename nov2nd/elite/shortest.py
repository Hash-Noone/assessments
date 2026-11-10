graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

def shortest_path(graph, start, goal): 
    #returns a list of nodes for one shortest path from start to goal, 
    # or [] if there is no path.
    pass

def reachable(graph, start): 
    #returns the number of nodes 
    # reachable from start, including start.
    pass

def has_cycle(graph): 
    #returns True if the graph contains a cycle.
    seen = set()
    stack = set()

    def dfs(current):
        seen.add(current)
        stack.add(current)
        if isinstance(current, list):
            for n in current:
                if dfs(current):
                    return True
            return False
        neighbor = graph.get(current)
        if neighbor:
            if isinstance(neighbor, list):
                for n in neighbor:
                    if dfs(neighbor):
                        return True
                return False
            if neighbor not in seen:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(current)
        return False

    for key in graph:
        if key not in seen:
            if dfs(key):
                return True
    return False

print(has_cycle(graph))
        