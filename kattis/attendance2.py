x=int(input())
names=[]
for _ in range(x):
    n=input()
    if n!="Present!":
        names.append(n)
    else:
        names=names[:-1]
if not names:
    print("No Absences")
else:
    for name in names:
        print(name)