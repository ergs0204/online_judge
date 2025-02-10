while 1:
	i=input()
	if i=="END":
		break
	t=1
	while i!="1":
		t+=1
		i=str(len(i))
	print(t)