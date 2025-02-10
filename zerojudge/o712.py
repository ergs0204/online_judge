m,n,k,r,c=map(int,input().split())
data=[]
for _ in range(m):
    data.append(list(map(int,input().split())))
gem=0
score=0

direction=[(0,1),(1,0),(0,-1),(-1,0)]
currentdir=0
while True:
    if data[r][c]==0:
        break
    score+=data[r][c]
    gem+=1
    data[r][c]-=1   
    if score%k==0:
        currentdir=(currentdir+1)%4
    nr=r+direction[currentdir][0]
    nc=c+direction[currentdir][1]
    while not (0<=nr<m) or not(0<=nc<n) or data[nr][nc]==-1:
        currentdir=(currentdir+1)%4
        nr=r+direction[currentdir][0]
        nc=c+direction[currentdir][1]
    r=nr
    c=nc
print(gem)