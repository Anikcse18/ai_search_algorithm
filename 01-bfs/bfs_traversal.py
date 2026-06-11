import collections

def bfs(graph, root,target=0):
    visited = set()
    queue = collections.deque([root])

    while queue:
        vertex =  queue.popleft();
       
        for neighbor in graph[vertex]:
            if neighbor not in visited :
                visited.add(neighbor)
                queue.append(neighbor)
    print("Visited nodes:", sorted(list(visited)))
    

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

  
    bfs(graph, "A")