def queen8(n,queen=[]):
    if len(queen)==n:
        ans.append(queen)
    for i in range(n):
        if valid(queen,i):
            queen8(n,queen+[i])
    return len(ans)
def valid(queen,nex):
    if any([abs(queen[i] - nex) in (0, len(queen) - i) for i in range(len(queen))]):
        return False
    if (len(queen),nex) in holes:
        return False
    return True

while 1:
    n,h=map(int,input().split())
    if n==h==0:
        break
    holes=set()
    for _ in range(h):
        inp=list(map(int,input().split()))
        holes.add((inp[0],inp[1]))
    ans=[]
    print(queen8(n))