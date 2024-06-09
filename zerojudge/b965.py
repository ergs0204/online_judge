def flip(matrix):
    return matrix[::-1]

def rotate(matrix):
    return list(zip(*matrix[::-1]))

def transform(matrix, operations):
    for operation in operations:
        if operation == 0:
            matrix = rotate(matrix)
        else:
            matrix = flip(matrix)
    return matrix

R, C, M = map(int, input().split())
matrix_B = [list(map(int, input().split())) for _ in range(R)]
operations = list(map(int, input().split()))

# Apply the inverse operations in reverse order
inverse_operations = operations[::-1]
for i in range(len(inverse_operations)):
    inverse_operations[i] = 1 - inverse_operations[i]

matrix_A = transform(matrix_B, inverse_operations)

# Output the result
print(len(matrix_A), len(matrix_A[0]))
for row in matrix_A:
    print(' '.join(map(str, row)))