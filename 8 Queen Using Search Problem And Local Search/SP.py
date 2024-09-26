from simpleai.search import SearchProblem, astar, greedy
import time


class EightQueens(SearchProblem):
    def __init__(self, initial_state=None):
        self.goal = tuple(range(8))
        initial_state = tuple([-1] * 8) if initial_state is None else initial_state
        super().__init__(initial_state)

    def actions(self, state):
        column = next((i for i, x in enumerate(state) if x == -1), 8)
        if column == 8:
            return []
        return [row for row in range(8) if self.is_safe(state, row, column)]

    def result(self, state, action):
        new_state = list(state)
        new_state[new_state.index(-1)] = action
        return tuple(new_state)

    def is_goal(self, state):
        return state == self.goal or (len(set(state)) == 8 and -1 not in state)

    def cost(self, state, action, state2):
        return 1

    def heuristic(self, state):
        return len([1 for i in range(8) if state[i] == -1])

    def is_safe(self, state, row, col):
        for i in range(col):
            if state[i] == row or \
               (state[i] != -1 and abs(state[i] - row) == abs(i - col)):
                return False
        return True

def solve_queens(algorithm, timeout=10):
    problem = EightQueens()
    start_time = time.time()
    
    if algorithm == 'astar':
        result = astar(problem, graph_search=True)
    elif algorithm == 'greedy':
        result = greedy(problem, graph_search=True)
    
    end_time = time.time()
    time_taken = end_time - start_time
    
    if time_taken > timeout:
        print(f"Search exceeded timeout of {timeout} seconds.")
        return None, time_taken
    
    return result, time_taken

def print_solution(result, time_taken):
    if result is None:
        print("No solution found within the time limit.")
    else:
        print(f"Solution found in {time_taken:.4f} seconds")
        print(f"Path length: {len(result.path())}")
        print("Solution:")
        final_state = result.state
        print_board(final_state)
        print(f"Total cost: {result.cost}")

def print_board(state):
    for row in range(8):
        line = ""
        for col in range(8):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    print("Solving Eight Queens problem with A* algorithm:")
    astar_result, astar_time = solve_queens('astar')
    print_solution(astar_result, astar_time)
    
    print("\nSolving Eight Queens problem with Greedy algorithm:")
    greedy_result, greedy_time = solve_queens('greedy')
    print_solution(greedy_result, greedy_time)