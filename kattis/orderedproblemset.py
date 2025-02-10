# read the data
l = int(input())
li = []
for _ in range(l):
    li.append(int(input()))
# def gcd


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# count every increase
c = 1
ll = []
for i in range(1, l):
    if li[i] > li[i - 1]:
        c += 1
    else:
        ll.append(c)
        c = 1
ll.append(c)
# print(ll)
# do gcd to every increase
x = ll[0]
for i in ll[1:]:
    x = gcd(x, i)

if x <= 1:
    print(-1)
else:
    for i in range(2, x + 1):
        if x % i == 0:
            print(i)

# 1 k problem in a set if set 符合
# 2 先找每一段increasing有幾個，找increasing的公因數 即為答案
