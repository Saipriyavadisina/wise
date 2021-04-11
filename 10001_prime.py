import math 

def my_prime(num):
    count=1
    if num==1:
        i=2
        print (i)
    else:
        i=3  
        while i>=3:
            for a in range(2, int(math.sqrt(i))+1):
                if i % a == 0:
                    break
            else:
                count+=1
                if count==num:
                    print (i)
                    break
            i+=2
    
    
my_prime (10001)
