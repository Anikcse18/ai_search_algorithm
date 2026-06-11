import unittest

from bfs_shortest_path import bfs_shortest_path, reconstruct


# The sample graph used across most tests (undirected, connected).
GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E", "F"],
    "D": ["B", "G"],
    "E": ["B", "C", "G", "H"],
    "F": ["C", "H"],
    "G": ["D", "E", "I"],
    "H": ["E", "F", "I"],
    "I": ["G", "H"],
}


def shortest_distance(graph, start, target):
    """Independent BFS that returns the hop count, used to validate path length."""
    import collections

    if start == target:
        return 0
    seen = {start}
    queue = collections.deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for nb in graph[node]:
            if nb not in seen:
                if nb == target:
                    return dist + 1
                seen.add(nb)
                queue.append((nb, dist + 1))
    return None


def is_valid_path(graph, path, start, target):
    """A path is valid if it starts/ends correctly and every step is an edge."""
    if not path or path[0] != start or path[-1] != target:
        return False
    return all(b in graph[a] for a, b in zip(path, path[1:]))


class TestBFSShortestPath(unittest.TestCase):
    def test_start_equals_target(self):
        # A zero-length journey returns just the node itself.
        self.assertEqual(bfs_shortest_path(GRAPH, "A", "A"), ["A"])

    def test_direct_neighbor(self):
        # Adjacent nodes -> path of length 2.
        self.assertEqual(bfs_shortest_path(GRAPH, "A", "B"), ["A", "B"])

    def test_path_is_valid(self):
        path = bfs_shortest_path(GRAPH, "A", "I")
        self.assertTrue(is_valid_path(GRAPH, path, "A", "I"))

    def test_shortest_length_A_to_E(self):
        # A->B->E or A->C->E, both length 3 (2 hops). BFS must not return longer.
        path = bfs_shortest_path(GRAPH, "A", "E")
        self.assertEqual(len(path), 3)
        self.assertTrue(is_valid_path(GRAPH, path, "A", "E"))

    def test_finds_minimum_hops_for_all_targets(self):
        # Cross-check BFS path length against an independent distance computation.
        for target in GRAPH:
            path = bfs_shortest_path(GRAPH, "A", target)
            self.assertIsNotNone(path, f"no path to {target}")
            self.assertEqual(
                len(path) - 1,
                shortest_distance(GRAPH, "A", target),
                f"non-minimal path to {target}: {path}",
            )

    def test_unreachable_returns_none(self):
        graph = {"A": ["B"], "B": ["A"], "X": ["Y"], "Y": ["X"]}
        self.assertIsNone(bfs_shortest_path(graph, "A", "X"))

    def test_single_node_graph(self):
        self.assertEqual(bfs_shortest_path({"A": []}, "A", "A"), ["A"])

    def test_linear_graph(self):
        graph = {"1": ["2"], "2": ["1", "3"], "3": ["2", "4"], "4": ["3"]}
        self.assertEqual(bfs_shortest_path(graph, "1", "4"), ["1", "2", "3", "4"])

    def test_directed_no_back_edge(self):
        # Directed graph: can reach C from A but not A from C.
        graph = {"A": ["B"], "B": ["C"], "C": []}
        self.assertEqual(bfs_shortest_path(graph, "A", "C"), ["A", "B", "C"])
        self.assertIsNone(bfs_shortest_path(graph, "C", "A"))

    def test_cycle_does_not_loop_forever(self):
        graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
        self.assertEqual(bfs_shortest_path(graph, "A", "C"), ["A", "B", "C"])


class TestReconstruct(unittest.TestCase):
    def test_reconstruct_chain(self):
        parent = {"A": None, "B": "A", "C": "B"}
        self.assertEqual(reconstruct(parent, "C"), ["A", "B", "C"])

    def test_reconstruct_single(self):
        self.assertEqual(reconstruct({"A": None}, "A"), ["A"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
