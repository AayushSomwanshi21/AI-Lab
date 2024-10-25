import heapq


def astar(graph: dict, heuristic: dict, start: str, goal: str):

    open_list = [(heuristic[start], start)]
    cost = {start: 0}
    path = {start: None}

    while open_list:

        curr_cost, curr_node = heapq.heappop(open_list)

        if curr_node == goal:

            path_list = [curr_node]
            total_cost = cost[curr_node]
            while path[curr_node] != None:
                path_list.append(path[curr_node])
                curr_node = path[curr_node]
            path_list.reverse()

            return path_list, total_cost

        for neigh, this_cost in graph[curr_node]:

            #  calc g(n)

            new_cost = cost[curr_node] + this_cost
            if neigh not in cost or new_cost < cost[neigh]:

                cost[neigh] = new_cost
                #  calc f(n) = g(n) + h(n)
                priority = heuristic[neigh] + new_cost
                heapq.heappush(open_list, (priority, neigh))
                path[neigh] = curr_node

    return -1


graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("D", 7), ("E", 3)],
    "C": [("F", 3), ("E", 1)],
    "D": [("G", 1)],
    "E": [("D", 2), ("G", 5)],
    "F": [("G", 2)],
    "G": []
}


heuristic = {
    "A": 10,
    "B": 8,
    "C": 7,
    "D": 4,
    "E": 2,
    "F": 4,
    "G": 0
}


start = "A"
goal = "G"

result = astar(graph, heuristic, start, goal)

if result:
    path, cost = result
    print(f"Shortest path from {start} to {goal}: {path}, Cost: {cost}")
else:
    print(f"No path found from {start} to {goal}")
