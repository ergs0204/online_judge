ans=set(input())
guess=list(input())
live=10
while live>0:
	g=guess.pop(0)
	if g in ans:
		ans.remove(g)
		if not len(ans):
			break
	else:
		live-=1
	# print(live)
if live:
	print("WIN")
else:
	print("LOSE")