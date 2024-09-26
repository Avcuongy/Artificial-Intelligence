import random

class EightQueensProblem:
    def __init__(self):
        self.goal = tuple(range(8))

    def generate_random_state(self):
        return tuple(random.sample(range(8), 8))

    def crossover(self, state1, state2):
        cut = random.randint(1, 7)
        return state1[:cut] + state2[cut:]

    def mutate(self, state):
        new_state = list(state)
        pos = random.randint(0,  7)
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


def genetic_algorithm(problem, population_size=100, generations=100, mutation_chance=0.2):
    population = [problem.generate_random_state() for _ in range(population_size)]
    
    for _ in range(generations):
        population = sorted(population, key=problem.fitness, reverse=True)
        
        if problem.is_goal(population[0]):
            return population[0]
        
        new_population = population[:2] 
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = problem.crossover(parent1, parent2)
            
            if random.random() < mutation_chance:
                child = problem.mutate(child)
            
            new_population.append(child)
        
        population = new_population
    
    return max(population, key=problem.fitness)

def backtracking(problem, state=(), depth=0):
    if len(state) == 8:
        return state if problem.is_goal(state) else None

    for row in range(8):
        if all(state[col] != row and abs(state[col] - row) != depth - col for col in range(depth)):
            result = backtracking(problem, state + (row,), depth + 1)
            if result is not None:
                return result
    return None

def print_board(state):
    for i in range(8):
        row = ['Q' if state[j] == i else '.' for j in range(8)]
        print(' '.join(row))
    print()

# Khởi tạo bài toán
problem = EightQueensProblem()

'''print("Initial state:")
initial_state = problem.generate_random_state()
print_board(initial_state)
print(f"Fitness: {problem.fitness(initial_state)}")'''

# Genetic Algorithm
print("\nGenetic Algorithm:")
result_ga = genetic_algorithm(problem)
print_board(result_ga)
print(f"Fitness: {problem.fitness(result_ga)}")

# Backtracking
print("\nBacktracking:")
result_bt = backtracking(problem)
if result_bt:
    print_board(result_bt)
    print(f"Fitness: {problem.fitness(result_bt)}")
else:
    print("No solution found with Backtracking.")