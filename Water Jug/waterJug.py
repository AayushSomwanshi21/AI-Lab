def solve(start_state, jug_cap, target):

    explored = set()
    start_state = tuple(start_state)
    path = dfs(start_state, jug_cap, target, explored)
    return path


def dfs(current_state: tuple, jug_cap: tuple, target: int, explored: set):

    jug1, jug2 = current_state

    if jug1 == target or jug2 == target:
        return [current_state]

    explored.add(current_state)

    successors = get_successors(current_state, jug_cap)

    for succ in successors:
        if succ not in explored:
            path = dfs(succ, jug_cap, target, explored)
            if path is not None:
                return [current_state] + path


def get_successors(current_state: tuple, jug_cap: tuple):

    jug1, jug2 = current_state
    jug1_cap, jug2_cap = jug_cap

    successors = []

    successors.append((jug1, jug2_cap))
    successors.append((jug1_cap, jug2))
    successors.append((jug1, 0))
    successors.append((0, jug2))

    amt_to_pour = min(jug1, jug2_cap - jug2)
    successors.append((jug1 - amt_to_pour, jug2 + amt_to_pour))

    amt_to_pour = min(jug1_cap - jug1, jug2)
    successors.append((jug1 + amt_to_pour, jug2 - amt_to_pour))

    return [s for s in successors if is_valid(s, jug_cap)]


def is_valid(s: tuple, jug_cap: tuple):

    jug1, jug2 = s
    jug1_cap, jug2_cap = jug_cap

    return 0 <= jug1 <= jug1_cap and 0 <= jug2 <= jug2_cap


jug_cap = (4, 3)
start_state = (0, 0)
target = 2
path = solve(start_state, jug_cap, target)
print(path)
