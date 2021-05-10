import math
sum1=0
for a in range(3,1000000):
    b=[]
    b=list(str(a))
    sum=0
    for i in b:
        sum+=math.factorial(int(i))
        if sum==a:
            sum1+=sum
        else:
            pass
print(sum1)
