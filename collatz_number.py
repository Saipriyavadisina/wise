def collatz(n) :
    a = 1
    while n > 1 :
        if n % 2 == 0 :
            n /= 2
        else :
            n = n * 3 + 1
        a += 1
    return a

max = 0
nb_max = 0
for i in range(1000000) :
    chaine = collatz(i)
    if chaine > max :
        nb_max =  i
        max = chaine
    del(chaine)
    # print(str(i / 1000000 * 100)[0:5], "%")
print(nb_max)
