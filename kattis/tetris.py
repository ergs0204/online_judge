shape = [
    [[0], [0, 0, 0, 0]],  # I
    [[0, 0]],  # O
    [[0, 0, 1], [1, 0]],  # S
    [[1, 0, 0], [0, 1]],  # Z
    [[0, 0, 0], [1, 0], [1, 0, 1], [0, 1]],  # T
    [[0, 0], [0, 1, 1], [2, 0], [0, 0, 0]],  # L
    [[0, 0], [1, 1, 0], [0, 2], [0, 0, 0]],  # J
]
n, block = map(int, input().split())
row = list(map(int, input().split()))
block -= 1
buttoms = shape[block]
count = 0
for buttom in buttoms:
    for start in range(n - len(buttom) + 1):
        valid = True
        base = row[start] - buttom[0]
        for test in range(1, len(buttom)):
            if row[start + test] - buttom[test] != base:
                valid = False
                break
        if valid:
            count += 1
print(count)