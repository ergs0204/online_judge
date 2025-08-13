n = int(input())
x = 0
while n > 0:
    x += n % 10
    x *= 10
    n //= 10
print(x//10)
