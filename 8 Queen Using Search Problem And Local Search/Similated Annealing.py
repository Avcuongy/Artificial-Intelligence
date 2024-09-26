import random
import math

class EightQueensProblem:
    def __init__(self):
        self.goal = tuple(range(8))

    def generate_random_state(self):
        return tuple(random.sample(range(8), 8))

    def mutate(self, state):
        new_state = list(state)
        pos = random.randint(0, 7)
        new_state[pos] = random.randint(0, 7)
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

def simulated_annealing(problem, max_iterations=10000, initial_temperature=1.0, cooling_rate=0.995):
    current_state = problem.generate_random_state()
    current_fitness = problem.fitness(current_state)
    temperature = initial_temperature

    for _ in range(max_iterations):
        if problem.is_goal(current_state):
            return current_state

        neighbor = problem.mutate(current_state)
        neighbor_fitness = problem.fitness(neighbor)

        if neighbor_fitness > current_fitness:
            current_state = neighbor
            current_fitness = neighbor_fitness
        else:
            delta_e = neighbor_fitness - current_fitness
            probability = math.exp(delta_e / temperature)
            if random.random() < probability:
                current_state = neighbor
                current_fitness = neighbor_fitness

        temperature *= cooling_rate

    return current_state

def print_board(state):
    for i in range(8):
        row = ['Q' if state[j] == i else '.' for j in range(8)]
        print(' '.join(row))
    print()

problem = EightQueensProblem()

# Simulated Annealing
print("\nSimulated Annealing:")
result_sa = simulated_annealing(problem)
print_board(result_sa)
print(f"Fitness: {problem.fitness(result_sa)}")