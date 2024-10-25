import heapq as pq


def uniform_cost_search(graph: dict, start: str, goal: str):

    queue = []
    visited = set()
    pq.heappush(queue, (0, start, []))

    while queue:

        curr_cost, curr_node, curr_path = pq.heappop(queue)
        updated_path = curr_path.copy()
        updated_path.append(curr_node)
        if curr_node == goal:

            print("Path", updated_path)
            print("Cost:", curr_cost)
            quit()
        visited.add(curr_cost)

        for neigh, cost in graph[curr_node].items():

            if neigh not in visited:
                new_cost = cost + curr_cost
                pq.heappush(queue, (new_cost, neigh, updated_path))
    return -1


graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'D': 1},
    'D': {}
}
start = 'A'
goal = 'D'
uniform_cost_search(graph, start, goal)
