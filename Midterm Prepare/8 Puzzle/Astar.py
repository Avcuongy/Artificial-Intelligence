from simpleai.search import astar, SearchProblem

initial_state = ((1, 2, 3), (8, 0, 7), (4, 5, 6))

goal_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))


class EightPuzzleProblem(SearchProblem):
    def actions(self, state):
        empty_row, empty_col = [
            (r, c) for r in range(3) for c in range(3) if state[r][c] == 0
        ][0]
        actions = []
        if empty_row > 0:
            actions.append("up")
        if empty_row < 2:
            actions.append("down")
        if empty_col > 0:
            actions.append("left")
        if empty_col < 2:
            actions.append("right")
        return actions

    def result(self, state, action):
        empty_row, empty_col = [
            (r, c) for r in range(3) for c in range(3) if state[r][c] == 0
        ][0]
        new_state = [list(row) for row in state]

        if action == "up":
            new_state[empty_row][empty_col], new_state[empty_row - 1][empty_col] = (
                new_state[empty_row - 1][empty_col],
                new_state[empty_row][empty_col],
            )
        elif action == "down":
            new_state[empty_row][empty_col], new_state[empty_row + 1][empty_col] = (
                new_state[empty_row + 1][empty_col],
                new_state[empty_row][empty_col],
            )
        elif action == "left":
            new_state[empty_row][empty_col], new_state[empty_row][empty_col - 1] = (
                new_state[empty_row][empty_col - 1],
                new_state[empty_row][empty_col],
            )
        elif action == "right":
            new_state[empty_row][empty_col], new_state[empty_row][empty_col + 1] = (
                new_state[empty_row][empty_col + 1],
                new_state[empty_row][empty_col],
            )

        return tuple(tuple(row) for row in new_state)

    def is_goal(self, state):
        return state == goal_state

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        return sum(
            abs(r1 - r2) + abs(c1 - c2)
            for r1 in range(3)
            for c1 in range(3)
            for r2 in range(3)
            for c2 in range(3)
            if state[r1][c1] != 0 and state[r1][c1] == goal_state[r2][c2]
        )


def print_solution(result):
    if result is None:
        print("No solution found.")
        return

    for action, state in result.path():
        if action is not None:
            print(f"Action: {action}")
        for row in state:
            print(row)
        print()


problem = EightPuzzleProblem(initial_state)
result = astar(problem)
print_solution(result)
