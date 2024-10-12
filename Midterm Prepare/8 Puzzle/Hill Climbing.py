from simpleai.search import SearchProblem, hill_climbing_random_restarts

INITIAL_STATE = ((1, 5, 2), (4, 0, 6), (7, 8, 3))

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

        state_list = list(list(row) for row in state)
        state_list[empty_row][empty_col], state_list[new_row][new_col] = (
            state_list[new_row][new_col],
            0,
        )

        return tuple(tuple(row) for row in state_list)

    def value(self, state):
        value = 0
        for r in range(3):
            for c in range(3):
                if state[r][c] != 0:
                    goal_r, goal_c = self.find_tile(GOAL_STATE, state[r][c])
                    if (r, c) != (goal_r, goal_c):
                        value -= 1
        return value

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

    def generate_random_state(self):
        import random

        random_state = list(GOAL_STATE)
        random.shuffle(random_state)
        for i in range(3):
            random_state[i] = tuple(random_state[i])
        return tuple(random_state)


problem = EightPuzzleProblem(initial_state=INITIAL_STATE)

restarts_limit = 20

result = hill_climbing_random_restarts(problem, restarts_limit=restarts_limit)

if result and result.state:
    print("Solution found:")
    print(result.state)
else:
    print("No solution found.")
