def Sum_Digits(n):
    Sum=0
    n=str(n)    
    for i in n:
       i=int(i) 
       Sum=i+Sum
    n=Sum
    return n
n=Sum_Digits(2**1000)
print(n)
