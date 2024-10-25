graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

visited = []


def dfs(node):
    print("Visited:", node)
    visited.append(node)
    for next in graph[node]:
        if next not in visited:
            dfs(next)


dfs('A')
