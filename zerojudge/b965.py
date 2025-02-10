def rotate(matrix):
    # 順時針旋轉90度
    R = len(matrix)
    C = len(matrix[0])
    result = [[0] * R for _ in range(C)]
    for i in range(R):
        for j in range(C):
            result[j][R-1-i] = matrix[i][j]
    return result

def flip(matrix):
    # 上下翻轉
    return matrix[::-1]

# 讀取輸入
R, C, M = map(int, input().split())
matrix_B = []
for _ in range(R):
    row = list(map(int, input().split()))
    matrix_B.append(row)
operations = list(map(int, input().split()))

# 反向執行操作以得到矩陣A
matrix = matrix_B
for op in operations[::-1]:
    if op == 0:  # 旋轉的反操作是逆時針旋轉3次
        matrix = rotate(rotate(rotate(matrix)))
    else:  # 翻轉的反操作還是翻轉
        matrix = flip(matrix)

# 輸出結果
print(len(matrix), len(matrix[0]))
for i, row in enumerate(matrix):
    print(' '.join(map(str, row)))
