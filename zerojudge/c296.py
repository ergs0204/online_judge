n,m,k=map(int,input().split())

people=[i+1 for i in range(n)]

for _ in range(k):
    for safe in range(m-1):
        people.append(people.pop(0))
    people.pop(0)

print(people[0])