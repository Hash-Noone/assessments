from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": ["F"],
    "F": []
}

def shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return []
    index = 0
    queue = [start]
    visted = {
        start : None
    }
    while index < len(queue):
        current = queue[index]
        index += 1
        if current == goal:
            break
        for neighbor in graph.get(current, []):
            if neighbor not in visted:
                queue.append(neighbor)
                visted[neighbor] = current
    if goal not in visted:
        return []
    n = len(queue.copy())
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visted[current]

    return path[::-1]

def reachable(graph, start): 
    #returns the number of nodes 
    # reachable from start, including start.
    if start not in graph:
        return 0
    index = 0
    queue = [start]
    visted = {start}
    while index < len(queue):
        current = queue[index]
        index += 1
        for neighbor in graph.get(current, []):
            if neighbor not in visted:
                queue.append(neighbor)
                visted.add(neighbor)
    return len(queue)

def has_cycles(graph):
    visited = set()

    for start in graph:
        if start in visited:
            continue

        queue = deque([(start, None)])
        visited.add(start)

        while queue:
            current, parent = queue.popleft()

            for neighbor in graph.get(current, []):

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current))

                elif neighbor != parent:
                    return True

    return False

def has_cycle(graph):
    in_degree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = [node for node, deg in in_degree.items() if deg == 0]
    i = 0

    while i < len(queue):
        node = queue[i]
        i += 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return len(queue) != len(graph)


def shortest_paths(graph, start, goal):
    if start not in graph or goal not in graph:
        return []

    queue = deque([start])
    distance = {start: 0}
    parents = {start: []}

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):

            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                parents[neighbor] = [current]
                queue.append(neighbor)

            elif distance[neighbor] == distance[current] + 1:
                parents[neighbor].append(current)

    if goal not in distance:
        return []

    paths = []

    def backtrack(node, path):
        if node == start:
            paths.append([start] + path)
            return

        for parent in parents[node]:
            backtrack(parent, [node] + path)

    backtrack(goal, [])

    return paths

print(shortest_paths(graph, "A", "F"))
        