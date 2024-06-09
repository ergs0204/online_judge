n=int(input())
seq=input()
ans=""
a=0
seen=set()
i=0
while a<n:
	now=seq[i]
	if now not in seen and len(seen)==2:
		ans+=now
		a+=1
		seen=set()
	elif now not in seen:
		seen.add(now)
	i+=1
print(ans)