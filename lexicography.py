import itertools
x = [p for i,p in enumerate(itertools.permutations(range(10))) if i == 999999]
print(x)
