def tokey(c):
	if c==" ":
		return '0',1
	elif "a"<=c<="o":
		# alphabat
		return str((ord(c)-ord('a'))//3+2),(ord(c)-ord('a'))%3+1
	elif c<="s":
		return "7",ord(c)-ord('p')+1
	elif c<="v":
		return str((ord(c)-ord('a')-1)//3+2),(ord(c)-ord('t'))%3+1
	else:
		return "9",ord(c)-ord('w')+1
n=int(input())
for i in range(n):
	w=input()
	key,count=tokey(w[0])
	s=key*count
	key_=key
	for c in w[1:]:
		key,count=tokey(c)
		if key==key_:
			s+=" "
		s+=key*count
		key_=key

	print(f"Case #{i+1}: {s}")