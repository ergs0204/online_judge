# datas={"date":[name,rate]}
datas={}

t=int(input())
for _ in range(t):
	n,r,d=input().split(" ")
	r=int(r)
	data=datas.get(d,None)
	if data==None:
		datas[d]=[n,r]
	elif data[1]<r:
		datas[d]=[n,r]

print(len(datas.keys()))
ans=[i[0] for i in datas.values()]
ans.sort()
for i in ans:
	print(i)
