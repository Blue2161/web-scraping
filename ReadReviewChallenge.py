def rand(exclude):
    r = None
    while r in exclude or r is None:
         r = random.randrange(1,10)
    return r
