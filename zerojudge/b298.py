n, m, l, q = map(int, input().split(" "))

badcompanies = set()
link = [[].copy() for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    link[a - 1].append(b - 1)

for _ in range(l):
    bad = int(input()) - 1
    if bad not in badcompanies:
        dos = {bad}
        while len(dos) > 0:
            doing = dos.pop()
            if doing not in badcompanies:
                badcompanies.add(doing)
                dos.update(link[doing])

for _ in range(q):
    ask = int(input()) - 1
    if ask in badcompanies:
        print("TUIHUOOOOOO")
    else:
        print("YA~~")
