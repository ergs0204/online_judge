def find_cycles(graph):
    """Find all cycles in the graph. Returns a list of cycles."""
    visited = set()
    stack = []
    cycles = []

    def dfs(node):
        if node in visited:
            if node in stack:
                cycles.append(stack[stack.index(node):])
            return
        visited.add(node)
        stack.append(node)
        if node in graph:
            dfs(graph[node])
        stack.pop()
    
    for node in graph:
        if node not in visited:
            dfs(node)
    return cycles

def solve_love_arrows(N, loves):
    graph = {s: t for s, t in loves}
    cycles = find_cycles(graph)

    arrows_needed = 0
    for cycle in cycles:
        # For each cycle, round up len(cycle) / 2 arrows are needed
        arrows_needed += (len(cycle) + 1) // 2

    return arrows_needed

# Sample Input 1
N1 = 8
loves1 = [
    ("leonard", "emmy"),
    ("ada", "emmy"),
    ("isaac", "leonard"),
    ("emmy", "pierre"),
    ("pierre", "bernhard"),
    ("bernhard", "emmy"),
    ("sofia", "karl"),
    ("karl", "sofia"),
]
print(solve_love_arrows(N1, loves1))  # Expected Output: 3

# Sample Input 2
N2 = 4
loves2 = [
    ("a", "c"),
    ("b", "c"),
    ("c", "d"),
    ("d", "d"),
]
print(solve_love_arrows(N2, loves2))  # Expected Output: 3

# Sample Input 3
N3 = 3
loves3 = [
    ("rocky", "scarlet"),
    ("scarlet", "patrick"),
    ("patrick", "rocky"),
]
print(solve_love_arrows(N3, loves3))  # Expected Output: 2