import numpy as np
import random

ls = np.random.randint(1, 99, (10, 10))


def find_neighbours(init_x, init_y):

    valid_states = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            x_val = init_x + i
            y_val = init_y + j

            if 0 < x_val < ls.shape[0] and 0 < y_val < ls.shape[1] and (x_val, y_val) != (init_x, init_y):
                valid_states.append((x_val, y_val))
    return valid_states


def hill_climbing():

    x = random.randint(0, ls.shape[0] - 1)
    y = random.randint(0, ls.shape[1] - 1)
    print(f"Start state:{x, y} with values:{ls[x][y]}")

    for i in range(50):

        neigh = find_neighbours(x, y)

        n_x, n_y = max(neigh, key=lambda coords: ls[coords[0]][coords[1]])

        if ls[n_x][n_y] <= ls[x][y]:
            break
        x, y = n_x, n_y
        print(f"Travelling to:{x, y} with value:{ls[x][y]}")
    return x, y


x, y = hill_climbing()
print(f"Optimal State:{x, y} with values:{ls[x][y]}")
