x = int(input())
s = input()
bs = []  # 0 small 1 big
for i in s:
    if "a" <= i <= "z":
        bs.append(0)
    else:
        bs.append(1)
c = []
now = bs[0]
count = 1
for i in bs[1:]:
    if i == now:
        count += 1
    else:
        c.append(count)
        now = i
        count = 1
c.append(count)
# print(c)
ans = 0
count = 0
for i in range(len(c)): 
    if c[i]>x:
        ans=max(ans,count+1)
        count=1
    elif c[i]==x:
        count+=1
    else:
        count=0
    ans=max(ans,count)
    # print(c[i],"count",count)
print(ans*x)
