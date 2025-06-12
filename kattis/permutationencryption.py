while True:
    len_, *key = map(int, input().split())
    if len_ == 0:
        break
    text = input()

    if len(text) % len_ != 0:
        text += " "*(len_-len(text) % len_)

    print("'", end="")
    for i in range(0, len(text), len_):
        for j in range(len_):
            print(text[i+key[j]-1], end="")
    print("'")
