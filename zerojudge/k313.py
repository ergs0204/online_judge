num, limit, price = map(int, input().split())
data = []
totalweight = 0
for _ in range(num):
    data.append(list(map(int, input().split())))
    totalweight += data[-1][0]

old = {0: 0}
for weight, throw in data:
    new = old.copy()
    for w, v in old.items():
        new[weight+w] = min(old.get(weight+w, float('inf')), throw+v)
    old = new

fee = float('inf')

for weight, throw in new.items():
    over = max(totalweight-weight-limit, 0)
    fee = min(fee, throw+over*price)

print(fee)
