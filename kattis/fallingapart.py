x=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
ans=[0,0]
for i in range(x):
    ans[i%2]+=data[i]
print(ans[0],ans[1])