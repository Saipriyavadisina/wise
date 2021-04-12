def voies(x, y) :
    droite = True
    bas = True
    if x == 0 :
        droite = False
    if y == 0 :
        bas = False
    return droite, bas

points = {v : [] for v in range(0, 41)}

for x in range(0, 21) :
    for y in range(0, 21) :
        points[x + y].append((x, y))

valeurs = {(0, 0) : 1}

for i in range(1, 41) :
    for v in points[i] :
        chemins = 0
        x, y = v
        droite, bas = voies(x, y)
        if droite :
            chemins += valeurs[(x-1, y)]
        if bas :
            chemins += valeurs[(x, y-1)]
        valeurs[v] = chemins
        print (v, ":", chemins)
