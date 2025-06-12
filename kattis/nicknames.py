import io
import sys

name_n=int(input())
names=[]
for _ in range(name_n):
    inp = io.BytesIO(sys.stdin.buffer.readline()).read().decode()
    names.append(inp.strip())
nick_n=int(input())
for _ in range(nick_n):
    nick=io.BytesIO(sys.stdin.buffer.readline()).read().decode().strip()
    count=0
    for name in names:
        # print(name,nick,len(name)>=len(nick),name[:len(nick)]==nick)
        if len(name)>=len(nick) and name[:len(nick)]==nick:
            count+=1
    sys.stdout.write(str(count)+"\n")