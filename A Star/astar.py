import heapq as pq


def astar(graph: dict, start: str, goal: str, heuristic: dict):

    visited = set()
    path = {start: None}  # closed list
    cost = {start: 0}
    open_list = [(heuristic[start], start)]

    while open_list:

        _, curr_node = pq.heappop(open_list)

        if curr_node == goal:
            final_cost = cost[curr_node]
            path_list = [curr_node]
            while path[curr_node] != None:
                path_list.append(path[curr_node])
                curr_node = path[curr_node]
            path_list.reverse()
            return path_list, final_cost

        visited.add(curr_node)

        for neigh in graph[curr_node]:

            # total path cost g(n)
            new_cost = cost[curr_node] + graph[curr_node][neigh]

            if neigh not in cost or new_cost < cost[neigh]:

                cost[neigh] = new_cost
                # calculating f(n)
                priority = new_cost + heuristic[neigh]
                pq.heappush(open_list, (priority, neigh))
                path[neigh] = curr_node

    return None


graph = {
    "A": {"B": 2, "E": 3},
    "B": {"C": 1, "G": 9},
    "C": {"B": 1},
    "D": {"E": 6, "G": 1},
    "E": {"D": 6, "A": 3},
    "G": {"B": 9, "D": 1}
}

# Define the heuristic (estimated cost to goal)
heuristic = {
    "A": 11,
    "B": 6,
    "C": 99,
    "D": 1,
    "E": 7,
    "G": 0
}

# Test the A* algorithm
start = "A"
goal = "G"

result = astar(graph, start, goal, heuristic)

if result:
    path, cost = result
    print(f"Shortest path from {start} to {goal}: {path}, Cost: {cost}")
else:
    print(f"No path found from {start} to {goal}")
