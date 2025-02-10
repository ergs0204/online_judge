def convolution(image, kernel, H, W, N, M):
    result_height = H - N + 1
    result_width = W - M + 1
    result = [[0 for _ in range(result_width)] for _ in range(result_height)]

    for i in range(result_height):
        for j in range(result_width):
            s = 0
            for ki in range(N):
                for kj in range(M):
                    s += image[i + ki][j + kj] * kernel[ki][kj]
            result[i][j] = s
    return result


# Read input
H, W, N, M = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(H)]
# for _ in range(H):
#     image.append(list(map(int,input().split(" "))))
kernel = [list(map(int, input().split())) for _ in range(N)]
kernel = kernel[::-1]
for i in range(N):
    kernel[i] = kernel[i][::-1]
# Perform convolution
result = convolution(image, kernel, H, W, N, M)
# Print result
for row in result:
    print(" ".join(map(str, row)))
