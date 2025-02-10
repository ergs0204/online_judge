while 1:
    try:
        adul,pupa,larv,e,r,s,n=map(int,input().split())
        adul_,pupa_,larv_=adul,pupa,larv
        for _ in range(n):
            larv=adul_*e
            pupa=larv_//r
            adul=pupa_//s
            # print(f"Week {_+1}:adult={adul},pupa={pupa},larva={larv}")
            adul_,pupa_,larv_=adul,pupa,larv
        print(adul_)
    except:
        break