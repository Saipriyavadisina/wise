E = {0, 1, 2, 3, 4, 5, 6, 8}
N = {2, 4, 6, 8}

union_EN = E.union(N)
print("Union of E and N is", union_EN)

intersection_EN = E.intersection(N)
print("Intersection of E and N is", intersection_EN)

difference_EN = E.difference(N)
print("Difference of E and N is", difference_EN)

symmetric_difference_EN = E.symmetric_difference(N)
print("Symmetric difference of E and N is", symmetric_difference_EN)
