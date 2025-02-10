def iterative_dfs(graph, start):
    stack = [(start, 0)]  # Stack contains tuples of (node, depth)
    visited = [False] * len(graph)
    max_depth, max_node = 0, start

    while stack:
        node, depth = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        if depth > max_depth:
            max_depth, max_node = depth, node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append((neighbor, depth + 1))

    return max_depth, max_node


# Read the input
N = int(input())
graph = [[] for _ in range(N)]

# Construct the tree
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Perform the first DFS to find the farthest node from node 0
_, farthest_node = iterative_dfs(graph, 0)

# Perform the second DFS from the farthest node to find the maximum distance
max_distance, _ = iterative_dfs(graph, farthest_node)

# Output the maximum distance
print(max_distance)
