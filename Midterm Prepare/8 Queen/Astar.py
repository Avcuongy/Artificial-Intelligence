from simpleai.search import SearchProblem, astar

class EightQueensProblem(SearchProblem):
    def __init__(self):
        initial_state = (0, tuple())
        super(EightQueensProblem, self).__init__(initial_state)

    def actions(self, state):
        row, queens = state
        if row >= 8:
            return []

        actions = []
        for col in range(8):
            if self.is_valid(queens, col):
                actions.append(col)
        return actions

    def result(self, state, action):
        row, queens = state
        new_queens = queens + (action,)
        return (row + 1, new_queens)

    def is_valid(self, queens, col):
        row = len(queens)
        for r, c in enumerate(queens):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def is_goal(self, state):
        return len(state[1]) == 8

    def heuristic(self, state):
        return 8 - len(state[1])


def print_solution(solution):
    board = [["." for _ in range(8)] for _ in range(8)]
    for row, col in enumerate(solution.state[1]):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))


problem = EightQueensProblem()
result = astar(problem)

if result:
    print_solution(result)
else:
    print("Không tìm thấy giải pháp.")
