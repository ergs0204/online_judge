# attr=("123","DSO","STO","RGP")

def valid(c1,c2,c3):
	same=0
	diff=0
	for i in range(4):
		if c1[i]==c2[i]==c3[i]:
			same+=1
		elif c1[i]!=c2[i] and c2[i]!=c3[i] and c1[i]!=c3[i]:
			diff+=1
	return same+diff==4


cards=[]
for _ in range(4):
	cards.extend(input().split())

ans=[]
for i in range(10):
	for j in range(i+1,11):
		for k in range(j+1,12):
		# print(i,j,third)
			if valid(cards[i],cards[j],cards[k]):
				ans.append([i+1,j+1,k+1])
if len(ans):
	for inds in ans:
		print(inds[0],inds[1],inds[2])
else:
	print("no sets")