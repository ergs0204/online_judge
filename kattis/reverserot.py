CH="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while 1:
	x=input().split()
	if len(x)==1:
		break
	n=int(x[0])
	s=x[1]
	for ch in s[::-1]:
		print(CH[(CH.index(ch)+n)%28],end="")
	print()