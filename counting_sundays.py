def leap_year(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False
month_lenght = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
i=1 
sundays=0
for year in range (1900,2001):
    if leap_year(year):
        month_lenght[2]=29
    else:
        month_lenght[2]=28
    for month in month_lenght:
        if i%7==0:
            sundays+=1
        i=i+month_lenght[month]
i=1
for year in range (1900,1901):
    if leap_year(year):
        month_lenght[2]=29
    else:
        month_lenght[2]=28
    for month in month_lenght:
        if i%7==0:
            sundays-=1
        i=i+month_lenght[month]     
print(sundays)
