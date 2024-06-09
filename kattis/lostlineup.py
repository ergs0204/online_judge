n = int(input())
    
ans = [0] * n  # Initialize a list of size n with 0s
ans[0] = 1  # Set the first element to 1
l=list(map(int,input().split(" ")))

for i in range(2, n+1):
    t = l[i-2]
    ans[t + 1] = i  # Assign i to the t+1th element of ans

for i in ans:
    print(i, end=" ")
