n=int(input())
data={}
ani=[]
an=set()
for _ in range(n):
    animal,count,loc=input().split()
    if animal not in an:
        ani.append(animal)
        an.add(animal)
    count=int(count)
    locd=data.get(loc,{})
    locd[animal]=locd.get(animal,0)+count
    data[loc]=locd

# def ind(item)
#     return ani.index(item[0])
# for loc in data:
#     locd=data[loc]
#     locd=dict(sorted(locd.items(),key=ind))
#     data[loc]=locd

s=""
for loc,locd in data.items():
    s+=loc+" : "
    sa=sorted(locd,key=ani.index)
    for animal in sa:
        s+=animal+" "+str(locd[animal])+", "
    s=s[:-2]
    s+="\n"
s=s[:-1]
print(s)