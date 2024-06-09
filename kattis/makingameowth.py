def reading_time(n,p,x,y):
    time = 0
    i=1
    while 1:
        is_meowth = (i % n == 0)
        if p == 0:
            if is_meowth:
                time += y
            break
        if is_meowth:
            time += y
        else:  # 主人讀
            time += x
            p -= 1
        i+=1
    print(time)


n,p,x,y = map(int, input().split())
reading_time(n,p,x,y)