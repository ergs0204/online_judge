n=int(input())
answer=[input() for _ in range(n)]
ans=sum([answer[i]==answer[i+1] for i in range(n-1)])
print(ans)