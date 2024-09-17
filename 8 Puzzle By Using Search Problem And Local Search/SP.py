
import os
from simpleai.search import SearchProblem, astar, greedy
import time

os.system("cls")

class EightPuzzle(SearchProblem):
    def __init__(self, initial_state):
        SearchProblem.__init__(self, initial_state)
        self.goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)

    def actions(self, state):
        empty = state.index(0)
        actions = []
        if empty not in [0, 1, 2]:
            actions.append('UP')
        if empty not in [6, 7, 8]:
            actions.append('DOWN')
        if empty not in [0, 3, 6]:
            actions.append('LEFT')
        if empty not in [2, 5, 8]:
            actions.append('RIGHT')
        return actions

    def result(self, state, action):
        empty = state.index(0)
        new_state = list(state)
        if action == 'UP':
            new_state[empty], new_state[empty - 3] = new_state[empty - 3], new_state[empty]
        elif action == 'DOWN':
            new_state[empty], new_state[empty + 3] = new_state[empty + 3], new_state[empty]
        elif action == 'LEFT':
            new_state[empty], new_state[empty - 1] = new_state[empty - 1], new_state[empty]
        elif action == 'RIGHT':
            new_state[empty], new_state[empty + 1] = new_state[empty + 1], new_state[empty]
        return tuple(new_state)

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return 1

    def heuristic(self, state):
        return sum(abs(state.index(i) - self.goal.index(i)) for i in range(1, 9))

def solve_puzzle(initial_state, algorithm, timeout=10):
    problem = EightPuzzle(initial_state)
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
        print("Solution path:")
        for i, (action, state) in enumerate(result.path()):
            print(f"Step {i}: Action: {action}")
            print_state(state)
        print(f"Total cost: {result.cost}")

def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) for x in state[i:i+3]))
    print()

if __name__ == "__main__":
    initial_state = (1, 2, 3, 8, 0, 7, 4, 5, 6)
    
    print("Initial state:")
    print_state(initial_state)
    
    print("\nSolving with A* algorithm:")
    astar_result, astar_time = solve_puzzle(initial_state, 'astar')
    print_solution(astar_result, astar_time)
    
    print("\nSolving with Greedy algorithm:")
    greedy_result, greedy_time = solve_puzzle(initial_state, 'greedy')
    print_solution(greedy_result, greedy_time)