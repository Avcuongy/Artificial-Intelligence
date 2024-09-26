import random

class EightQueensProblem:
    def __init__(self):
        self.goal = tuple(range(8))

    def generate_random_state(self):
      
        return tuple(random.sample(range(8), 8))

    def mutate(self, state):
        
        new_state = list(state)
        idx = random.randint(0, 7)
        new_value = random.choice(list(set(range(8)) - {new_state[idx]}))
        new_state[idx] = new_value
        return tuple(new_state)

    def fitness(self, state):
        
        conflicts = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    conflicts += 1
        return 28 - conflicts 

    def is_goal(self, state):

        return self.fitness(state) == 28

def hill_climbing(problem, max_iterations=1000):
    current_state = problem.generate_random_state()
    for _ in range(max_iterations):
        if problem.is_goal(current_state):
            return current_state

        neighbors = [problem.mutate(current_state) for _ in range(8)]
        best_neighbor = max(neighbors, key=problem.fitness)

        if problem.fitness(best_neighbor) <= problem.fitness(current_state):
            current_state = problem.generate_random_state()
        else:
            current_state = best_neighbor
    return current_state
def print_board(state):
    for i in range(8):
        row = ['Q' if state[j] == i else '.' for j in range(8)]
        print(' '.join(row))
    print()

problem = EightQueensProblem()

print("\nHill Climbing with Random Restart:")
result_hc = hill_climbing(problem)
print_board(result_hc)
print(f"Fitness: {problem.fitness(result_hc)}")
