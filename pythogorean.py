def Pethagoras(a,b,c):
    d=(a**2)+(b**2)
    if d==(c**2):
        return True
    return False
n=200
counter=0
for i in range(n,999):
    for j in range(n +1,999):
        for x in range(n +2,999):

            if Pethagoras(i, j, x):
                counter = i + j + x

                if counter == 1000:
                    multi = i * j * x
                    print(multi)
                    break
                else:
                    continue
            else:
                continue
