graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

queue = []
visited = []


def bfs(start):

    # visited.append(start)
    queue.append(start)
    while queue:

        m = queue.pop(0)
        print(m, end=' ')

        for neigh in graph[m]:

            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)


bfs("A")
