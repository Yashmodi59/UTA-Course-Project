def heuristic_expense(state, goal_state) -> int:
    total_cost = 0  # Initialize the total cost
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                # Calculate the Manhattan distance of the tile in the current state
                current_row, current_col = i, j
                goal_row, goal_col = find_pos_of_data(goal_state, tile)
                manhattan_dist = abs(current_row - goal_row) + abs(current_col - goal_col)
                # Add the cost of moving the tile to the Manhattan distance
                total_cost += manhattan_dist * tile
    return total_cost


def find_pos_of_data(matrix, data):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == data:
                return i, j


def get_solution_path(actual_state):
    solution = []
    while actual_state.parent is not None:
        solution.append(actual_state.move)
        actual_state = actual_state.parent
    solution.reverse()
    return solution


def get_neighbourhood_pos(x, y):
    all_pos = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
    val_pos = []
    for pos in all_pos:
        if 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2:
            val_pos.append(pos)
    return val_pos


def get_move(neighbour_pos, zero_pos):
    p, q = neighbour_pos
    x, y = zero_pos
    if p < x and q == y:
        return "Down"
    elif p == x and q < y:
        return "Right"
    elif p > x and q == y:
        return "Up"
    elif p == x and q > y:
        return "Left"
