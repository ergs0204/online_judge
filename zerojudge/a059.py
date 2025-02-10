n=int(input())
for i in range(n):
    s=int(int(input())**0.5)
    e=int(int(input())**0.5)
    ans=e*(e+1)*(2*e+1)//6-s*(s+1)*(2*s+1)//6
    print(f"Case {i+1}: {ans}")