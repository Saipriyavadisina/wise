from decimal import *
len_number = 950
getcontext().prec = len_number
n = 4 # length of the test string
candidate = set()

for a in range(2, 1000):
    x = str(Decimal(1)/Decimal(a))[3:]
    if len(x) >= len_number:
        test = x[-n-3:-3:] # get test string of n characters long, located at the end of x,
        # skipping the last 3 characters from the right end of x.
        # 3 because of a change that x=0.2345 ..799 will be rounded as x=0.2345 ..800
        if test.count(test[0]) != len(test): #if test does not consist the same elements, e.g. "33333"
            if test.count(test[0:1]) == 1: # get rid of the situation like "1010101010"
                if x.count(test) == 1 : 
                    candidate.add(a)
                    print(a)
                    # now choose one of four candidates, e.g. this one - 983
print(len(candidate))
