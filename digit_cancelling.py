from sympy import divisors
d,e=1,1
for i in range(11,100):
    for j in range(10,i):
        a=set()
        c=0
        a.add(i//10)
        a.add(i%10)
        a.add(j//10)
        a.add(j%10)
        b=list(a)
        if len(a)==3:
            c=i//10+i%10+j//10+j%10-b[0]-b[1]-b[2]
            if c!=0:
                if (i//10+i%10-c)!=0:
                    if (j//10+j%10-c)/(i//10+i%10-c)==j/i:
                        d,e=d*(j//10+j%10-c),e*(i//10+i%10-c)
f=divisors(d)
f.reverse()
for i in f:
    if e%i==0:
        e=e//i
        break
print(e)
