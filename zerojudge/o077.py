H,W,N=map(int,input().split())
board=[[0 for _ in range(W)] for __ in range(H)]
for i in range(N):
    r,c,t,x=map(int,input().split())
    for h_shift in range(t+1):
        for line in set([r+h_shift,r-h_shift]):
            if 0<=line<W:
                left=max(0,c-(t-h_shift))
                right=min(W,c+(t-h_shift)+1)
                for elem in range(left,right):
                    board[line][elem]+=x

for i in board:
    print(*board)