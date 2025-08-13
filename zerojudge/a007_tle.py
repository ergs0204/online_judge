while 1:
    try:
        number=int(input())
        x=True
        for i in range(2,number):
            if number%i==0:
                x=False
                break
        if x:
            print("Prime")
        else:
            print("Not Prime")
    except:
        break