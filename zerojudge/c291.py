n=int(input())
friends=list(map(int,input().split()))
done=[False for _ in range(n)]
loop=0
for i in range(n):
    if done[i]==False:
        #find loop
        start=i
        now=friends[i]
        done[i]=True
        while now!=start:
            done[now]=True
            now=friends[now]
        loop+=1
print(loop)