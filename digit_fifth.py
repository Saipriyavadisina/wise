sum(filter(lambda x: x == sum(map(lambda y: int(y)**5, str(x))), range(2, 1_000_000)))
