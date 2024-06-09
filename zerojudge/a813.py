from collections import deque

def solve(arr,n):
  ans = 0
  stack = deque()
  cnt = deque()
  for num in arr:
    while stack and stack[-1] < num:
      ans += cnt[-1]
      cnt.pop()
      stack.pop()
    if stack and stack[-1] == num:
      cnt[-1] += 1
    else:
      stack.append(num)
      cnt.append(1)
    if len(stack) > 1:
      ans += 1
  return ans * 2

# Test case
x=int(input())
b=list(map(int,input().split()))
print(solve(b,x))