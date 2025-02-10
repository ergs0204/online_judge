def check_year(year):
    year = str(year)
    for num in year:
        if year.count(num) > 1:
            return True
    return False


year = int(input()) + 1
while check_year(year):
    year += 1
print(year)
