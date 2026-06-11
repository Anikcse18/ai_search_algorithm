# 01 — Breadth-First Search (BFS)

This assignment demonstrates **Breadth-First Search (BFS)** on an undirected graph
through two programs:

| File | What it does |
|------|--------------|
| [bfs_traversal.py](bfs_traversal.py) | Visits every node reachable from a start node, level by level. |
| [bfs_shortest_path.py](bfs_shortest_path.py) | Finds the shortest path (fewest edges) between two nodes. |

---

## What is BFS?

BFS explores a graph **one layer at a time**. Starting from a node, it first visits
all of its direct neighbors, then all of *their* neighbors, and so on. It uses a
**queue** (first-in, first-out), which guarantees that nodes are reached in order of
increasing distance from the start.

Because it always reaches closer nodes before farther ones, BFS naturally finds the
**shortest path** in an unweighted graph.

---

## The graph used in both files

Both programs run on the same example graph (an undirected graph stored as an
adjacency list — each key maps to the list of its neighbors):

```
        A
       / \
      B   C
     /|   |\
    D E   E F
    |  \ / \ |
    G   (E)  H
     \  / \ /
      G    I
       \  /
        I
```

```python
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
```

---

## 1. BFS Traversal — [bfs_traversal.py](bfs_traversal.py)

**Goal:** visit and list every node that can be reached from a starting node.

**How it works:**
1. Put the start node in a queue.
2. Repeatedly take the front node out of the queue.
3. For each of its neighbors that we have **not visited yet**, mark it visited and
   add it to the back of the queue.
4. Continue until the queue is empty.

A `set` is used to track visited nodes so we never process the same node twice (this
also prevents infinite loops on cyclic graphs).

**Run it:**
```bash
python bfs_traversal.py
```

**Output:**
```
Visited nodes: ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
```

This confirms every node reachable from `A` was discovered.

---

## 2. BFS Shortest Path — [bfs_shortest_path.py](bfs_shortest_path.py)

**Goal:** find the shortest path (fewest edges) from a `start` node to a `target` node.

**How it works:**
1. Run BFS from the start node.
2. Each time we discover a new node, remember **which node discovered it** in a
   `parent` dictionary (e.g. `parent["E"] = "B"` means we reached `E` from `B`).
3. As soon as we discover the `target`, stop searching.
4. **Reconstruct** the path by walking backward through the `parent` links from the
   target to the start, then reverse it.

Because BFS reaches each node by the shortest possible route, the first time we see
the target *is* the shortest path. If the target can never be reached, the function
returns `None`.

**Run it:**
```bash
python bfs_shortest_path.py
```

**Output (start = `A`, target = `E`):**
```
['A', 'B', 'E']
```

So the shortest path from `A` to `E` is `A → B → E` (2 edges).

You can try other pairs by editing the `start` and `target` variables at the bottom
of the file.

---

## Key ideas to remember

- **Queue (FIFO)** is what makes the search "breadth-first."
- A **visited / seen set** stops repeated work and infinite loops.
- A **parent map** turns a plain traversal into a path finder.
- On an **unweighted** graph, BFS always gives the shortest path.
- Time complexity: **O(V + E)** — every vertex and edge is examined once.

---

## How to run

Requires Python 3 (no external libraries — only the built-in `collections` module).

```bash
cd 01-bfs
python bfs_traversal.py
python bfs_shortest_path.py
```
