import heapq as pq


def best_first_search(heuristic: dict, graph: dict, start: str, goal: str):

    open_list = [(heuristic[start], start, [start])]
    visited = set()

    while open_list:

        _, curr_node, curr_path = pq.heappop(open_list)

        if curr_node == goal:
            return curr_path

        visited.add(curr_node)

        for neigh, cost in graph[curr_node]:

            if neigh not in visited:
                pq.heappush(
                    open_list, (heuristic[neigh], neigh, curr_path + [neigh]))
    return None


heuristics = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 0,
}
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': [('E', 3)], 'E': []
}
start_node = 'A'
goal_node = 'E'
path = best_first_search(heuristics, graph, start_node, goal_node)
if path:
    print("Path found:", " -> ".join(path))
else:
    print("Path not found.")
