x, y, z = map(int, input().split(" "))
# first cases
if x / y == z:
    print(f"{x}/{y}={z}")
elif x * y == z:
    print(f"{x}*{y}={z}")
elif x + y == z:
    print(f"{x}+{y}={z}")
elif x - y == z:
    print(f"{x}-{y}={z}")
elif x == y / z:
    print(f"{x}={y}/{z}")
elif x == y - z:
    print(f"{x}={y}-{z}")
