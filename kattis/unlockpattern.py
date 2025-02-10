def distance(c1, c2):
    x1, y1 = c1[0], c1[1]
    x2, y2 = c2[0], c2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


pattern = [list(map(int, input().split(" "))) for _ in range(3)]
data = [0 for _ in range(9)]
for x in range(3):
    for y in range(3):
        data[pattern[x][y] - 1] = [x, y]
ans = 0
for i in range(8):
    c1 = data[i]
    c2 = data[i + 1]
    ans += distance(c1, c2)
print(ans)
