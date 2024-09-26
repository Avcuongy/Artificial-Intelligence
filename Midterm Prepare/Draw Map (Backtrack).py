variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']

# Miền giá trị cho mỗi biến (3 màu)
domains = {
    'WA': ['red', 'green', 'blue'],
    'NT': ['red', 'green', 'blue'],
    'Q': ['red', 'green', 'blue'],
    'NSW': ['red', 'green', 'blue'],
    'V': ['red', 'green', 'blue'],
    'SA': ['red', 'green', 'blue'],
    'T': ['red', 'green', 'blue']
}

# Các ràng buộc giữa các vùng lân cận
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'V', 'SA'],
    'V': ['NSW', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T': []
}

def is_consistent(assignment, var, value):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

# Thuật toán Backtracking
def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    unassigned_vars = [v for v in variables if v not in assignment]

    var = unassigned_vars[0]

    for value in domains[var]:
        if is_consistent(assignment, var, value):
            assignment[var] = value
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]

    return None

solution = backtrack({})
print(solution)