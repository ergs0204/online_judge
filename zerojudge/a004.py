# 西元年被4整除且不被100整除，或被400整除者即為閏年
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


while 1:
    try:
        year = int(input())
        if is_leap_year(year):
            print("閏年")
        else:
            print("平年")
    except:
        break
