def bfs(curr_state: tuple, goal_state: tuple):

    queue = [[curr_state]]
    explored = set()
    while queue:

        path = queue.pop(0)
        node = path[-1]

        # print("Path:", path)
        # print("Node:", node)
        if node == goal_state:
            return path

        successors = get_successors(node)

        for succ in successors:

            if succ not in explored:
                explored.add(succ)
                new_path = list(path)
                new_path.append(succ)
                queue.append(new_path)
    return None


def get_successors(curr_state: tuple):

    successors = []

    for i in range(3):
        for j in range(3):

            if i+j < 1 or i+j > 2:
                continue

            # If boat on left side
            if curr_state[2] == 1:
                child = ((curr_state[0][0] - i, curr_state[0][1] - j),
                         (curr_state[1][0] + i, curr_state[1][1] + j), 0)

            # If boat on right side
            else:
                child = ((curr_state[0][0] + i, curr_state[0][1] + j),
                         (curr_state[1][0] - i, curr_state[1][1] - j), 1)

            if is_valid(child):
                successors.append(child)
    return successors


def is_valid(child: tuple):

    if child[0][0] < child[0][1] and child[0][0] > 0:
        return False
    if child[1][0] < child[1][1] and child[1][0] > 0:
        return False

    return True


initial_state = ((3, 3), (0, 0), 1)
final_state = ((0, 0), (3, 3), 0)
path = bfs(initial_state, final_state)
print(path)
