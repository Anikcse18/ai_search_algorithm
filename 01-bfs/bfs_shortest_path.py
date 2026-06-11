import collections

def bfs_shortest_path(graph, start, target):
    if start == target:
        return [start]

    seen = {start} #seen but not yet processed
    parent = {start: None}                # NEW: who reached each node
    queue = collections.deque([start])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                parent[neighbor] = vertex  # NEW: remember the discoverer
                if neighbor == target:     # NEW: stop on discovery
                    return reconstruct(parent, target)
                queue.append(neighbor)
    return None                            # target unreachable

def reconstruct(parent, target):
    path, node = [], target
    while node is not None:
        path.append(node)
        node = parent[node]                # walk backward to the start
    return path[::-1]                       # reverse: start → ... → target
    

if __name__ == "__main__":
    
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "E", "F"],
        "D": ["B", "G"],
        "E": ["B", "C", "G", "H"],
        "F": ["C", "H"],
        "G": ["D", "E", "I"],
        "H": ["E", "F", "I"],
        "I": ["G", "H"]
    }
    start = "A"
    target = "E"

    print(bfs_shortest_path(graph, start, target))