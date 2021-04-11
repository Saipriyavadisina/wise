def sum_prime(n):
    def sieve(n):
        l = []
        prime = [True for i in range(n+1)] 
        p = 2 
        while (p*p <= n):
            if(prime[p] ==True):
                for i in range(p*2, n+1, p):
                    prime[i] = False
            p+=1
        prime[0] = False 
        prime[1] = False 
        for p in range(n+1):
            if prime[p]:
                l.append(p)
        return l
    primes = sieve(n)
    sum = 0
    for num in primes:
        sum += num
    print(sum)
sum_prime(2000000)
