last_sun,sun_t=map(int,input().split())
last_moon,moon_t=map(int,input().split())

for year in range(sun_t*moon_t):
    if (year+last_sun)%sun_t==0 and (year+last_moon)%moon_t==0:
        print(year)
        break