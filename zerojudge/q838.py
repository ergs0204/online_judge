n, t = map(int, input().split())

arr = list(map(int, input().split()))

st = []
ans = 0

for x in arr:
    while st and st[-1] <= x:
        ans += st[-1]
        x += st[-1]
        st.pop()
    if x <= t:
        st.append(x)

ans += sum(st)
print(ans)
