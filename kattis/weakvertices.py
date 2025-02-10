while True:
	x=int(input())
	if x==-1:
		break
	data=dict()
	for i in range(x):
		d=list(map(int,input().split()))
		data[i]=[i for i in range(x) if d[i]==1]
	tri=set()
	for i in range(x):
		if i not in tri:
			childs=data[i]
			found=False
			for j in range(len(childs)-1):
				for k in range(j+1,len(childs)):
					if childs[k] in data[childs[j]]:
						tri.add(childs[k])
						tri.add(childs[j])
						found=True
						break
				if found:
					break
			if not found:
				print(i,end=" ")
	print()

