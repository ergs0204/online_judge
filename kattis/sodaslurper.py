ans = 0
s, d, r = map(int, input().split(" "))

bottles = s + d

while bottles >= r:
    change = bottles // r
    left = bottles % r
    ans += change
    bottles = change + left

print(ans)
