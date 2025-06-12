n, cap = map(int, input().split())
weights = map(int, input().split())
values = map(int, input().split())

backpack = {0: 0}  # weight : value
for w, v in zip(weights, values):
    # backpack[w]=max(backpack.get(w,0),v)
    kv = list(backpack.items())
    for key, value in kv:
        backpack[key+w] = max(backpack.get(key+w, 0), value+v)

print(max(v for w, v in backpack.items() if w <= cap))
