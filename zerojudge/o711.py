n = int(input())
w1, w2, h1, h2 = map(int, input().split())
water = list(map(int, input().split()))
ans = 0
total = 0
last_height = 0
max_volume = w1*w1*h1 + w2*w2*h2  # 水杯最大容量

for w in water:
    total = min(total + w, max_volume)  # 限制總水量不超過杯子容量
    if total <= w1*w1*h1:
        height = total/(w1*w1)
    else:
        height = min(h1 + (total-w1*w1*h1)/(w2*w2), h1 + h2)  # 限制最大高度
    ans = max(height-last_height, ans)
    last_height = height
print(int(ans))