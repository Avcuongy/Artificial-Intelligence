import os
from simpleai.search import SearchProblem
from simpleai.search.local import genetic

# Define the goal state of the puzzle
GOAL = ((1, 2, 3),
        (8, 0, 4),
        (7, 6, 5))

class EightPuzzleProblem(SearchProblem):
    def actions(self, state):
        rows, cols = len(state), len(state[0])
        empty_row, empty_col = next((r, c) for r in range(rows) for c in range(cols) if state[r][c] == 0)
        
        actions = []
        if empty_row > 0:
            actions.append("UP")
        if empty_row < rows - 1:
            actions.append("DOWN")
        if empty_col > 0:
            actions.append("LEFT")
        if empty_col < cols - 1:
            actions.append("RIGHT")
        
        return actions

    def result(self, state, action):
        rows, cols = len(state), len(state[0])
        empty_row, empty_col = next((r, c) for r in range(rows) for c in range(cols) if state[r][c] == 0)
        
        new_state = [list(row) for row in state]
        
        if action == "UP":
            new_state[empty_row][empty_col], new_state[empty_row - 1][empty_col] = new_state[empty_row - 1][empty_col], new_state[empty_row][empty_col]
        elif action == "DOWN":
            new_state[empty_row][empty_col], new_state[empty_row + 1][empty_col] = new_state[empty_row + 1][empty_col], new_state[empty_row][empty_col]
        elif action == "LEFT":
            new_state[empty_row][empty_col], new_state[empty_row][empty_col - 1] = new_state[empty_row][empty_col - 1], new_state[empty_row][empty_col]
        elif action == "RIGHT":
            new_state[empty_row][empty_col], new_state[empty_row][empty_col + 1] = new_state[empty_row][empty_col + 1], new_state[empty_row][empty_col]
        
        return tuple(tuple(row) for row in new_state)

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        distance = 0
        for r in range(3):
            for c in range(3):
                val = state[r][c]
                if val != 0:
                    goal_r, goal_c = next((gr, gc) for gr in range(3) for gc in range(3) if GOAL[gr][gc] == val)
                    distance += abs(goal_r - r) + abs(goal_c - c)
        return distance

    def backtracking(self, state, path=[], visited=set(), depth=0, max_depth=20):
        if self.is_goal(state):
            return path

        if depth > max_depth:
            return None

        visited.add(state)

        for action in self.actions(state):
            new_state = self.result(state, action)
            if new_state not in visited:
                result = self.backtracking(new_state, path + [action], visited, depth + 1, max_depth)
                if result is not None:
                    return result
        return None

def manual_hill_climbing(problem):
    current_state = problem.initial_state
    current_path = []
    
    while True:
        neighbors = []
        for action in problem.actions(current_state):
            neighbor_state = problem.result(current_state, action)
            neighbors.append((neighbor_state, action))
        
        if not neighbors:
            return None
        
        next_state, action = min(neighbors, key=lambda x: problem.heuristic(x[0]))
        
        if problem.is_goal(next_state):
            return current_path + [action]
        
        if problem.heuristic(next_state) >= problem.heuristic(current_state):
            return None
        
        current_state = next_state
        current_path.append(action)
        
        # Debugging output
        print(f"Current state: {current_state}")
        print(f"Next state: {next_state}")
        print(f"Current path: {current_path}")

# Define the initial state of the puzzle
initial_state = ((1, 2, 3),
                 (8, 0, 7),
                 (4, 5, 6))

# Create an instance of the problem
problem = EightPuzzleProblem(initial_state)

# Hill Climbing search
print("Hill Climbing:")
try:
    result_hc = manual_hill_climbing(problem)
    if result_hc:
        print("Kết quả Hill Climbing (hành động):", result_hc)
        final_state_hc = initial_state
        for action in result_hc:
            final_state_hc = problem.result(final_state_hc, action)
        print("Trạng thái cuối cùng của Hill Climbing:", final_state_hc)
        if final_state_hc == GOAL:
            print("Hill Climbing solved the puzzle!")
        else:
            print("Hill Climbing did not solve the puzzle.")
    else:
        print("Hill Climbing did not find a solution.")
except Exception as e:
    print(f"An error occurred during Hill Climbing: {e}")

# Genetic Algorithm search
print("\nGenetic Algorithm:")
try:
    population_size = 100
    mutation_chance = 0.2
    result_ga = genetic(problem, population_size=population_size, mutation_chance=mutation_chance)
    print("Kết quả Genetic Algorithm:", result_ga.state)

    if result_ga.state == GOAL:
        print("Genetic Algorithm solved the puzzle!")
    else:
        print("Genetic Algorithm did not solve the puzzle.")
    print("Trạng thái cuối cùng của Genetic Algorithm:", result_ga.state)
except ImportError:
    print("Genetic Algorithm search is not available in the current environment.")
except Exception as e:
    print(f"An error occurred during Genetic Algorithm search: {e}")

# Backtracking search with depth limit
print("\nBacktracking:")
path_bt = problem.backtracking(initial_state)
if path_bt:
    final_state_bt = initial_state
    for action in path_bt:
        final_state_bt = problem.result(final_state_bt, action)
    print("Kết quả Backtracking (hành động):", path_bt)
    print("Trạng thái cuối cùng của Backtracking:", final_state_bt)
    
    if final_state_bt == GOAL:
        print("Backtracking solved the puzzle!")
else:
    print("Không tìm thấy giải pháp với Backtracking.")
