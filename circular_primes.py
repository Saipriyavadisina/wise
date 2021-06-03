import sympy as sp
def pe35(n):
    a=list(sp.primerange(2,n))
    c=[]
    for i in a:
        b=i
        while True:
            i=int(str(i)[-1]+str(i)[0:-1])
            if i==b:
                c.append(b)
                break
            if sp.isprime(i)==True:
                pass
            else:
                break
    return len(c)
print(pe35(1000000))
