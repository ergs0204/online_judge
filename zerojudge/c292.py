def spiral_traversal(matrix, start_direction):
    N = len(matrix)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # left, up, right, down
    turn_right = {0: 1, 1: 2, 2: 3, 3: 0}

    # Start from the center of the matrix
    x, y = N // 2, N // 2
    direction = start_direction
    steps = 1

    result = []

    while steps < N:
        for _ in range(2):  # Each distance is covered twice before incrementing
            for _ in range(steps):
                if 0 <= x < N and 0 <= y < N:
                    result.append(matrix[x][y])
                dx, dy = directions[direction]
                x, y = x + dx, y + dy
            direction = turn_right[direction]  # Turn right
        steps += 1

    # Cover the last leg of the spiral
    for _ in range(steps):
        if 0 <= x < N and 0 <= y < N:
            result.append(matrix[x][y])
        dx, dy = directions[direction]
        x, y = x + dx, y + dy

    return result

# Read the input
N = int(input())
start_direction = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# Perform the spiral traversal and output the result
print(''.join(map(str, spiral_traversal(matrix, start_direction))))