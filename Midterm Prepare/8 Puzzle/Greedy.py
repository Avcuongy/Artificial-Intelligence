from simpleai.search import SearchProblem, greedy

INITIAL_STATE = ((1, 2, 3), (8, 0, 7), (4, 5, 6))

GOAL_STATE = ((1, 2, 3), (8, 0, 4), (7, 6, 5))


class EightPuzzleProblem(SearchProblem):
    def actions(self, state):
        actions = []
        empty_row, empty_col = self.find_empty(state)
        possible_moves = [
            ("up", -1, 0),
            ("down", 1, 0),
            ("left", 0, -1),
            ("right", 0, 1),
        ]
        for move, delta_row, delta_col in possible_moves:
            new_row, new_col = empty_row + delta_row, empty_col + delta_col
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                actions.append((move, new_row, new_col))
        return actions

    def result(self, state, action):
        move, new_row, new_col = action
        empty_row, empty_col = self.find_empty(state)
        state_list = [list(row) for row in state]
        state_list[empty_row][empty_col], state_list[new_row][new_col] = (
            state_list[new_row][new_col],
            0,
        )
        return tuple(tuple(row) for row in state_list)

    def is_goal(self, state):
        return state == GOAL_STATE

    def heuristic(self, state):
        distance = 0
        for r in range(3):
            for c in range(3):
                value = state[r][c]
                if value != 0:
                    goal_r, goal_c = self.find_tile(GOAL_STATE, value)
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    def find_empty(self, state):
        for r in range(3):
            for c in range(3):
                if state[r][c] == 0:
                    return r, c

    def find_tile(self, state, tile):
        for r in range(3):
            for c in range(3):
                if state[r][c] == tile:
                    return r, c


problem = EightPuzzleProblem(initial_state=INITIAL_STATE)

result = greedy(problem)

if result and result.state:
    print("Solution found:")
    print(result.state)
else:
    print("No solution found.")
