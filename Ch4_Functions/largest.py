def maximum(values):
    large = None
    for value in values:
        if large is None or value > large:
            large = value
    return large

print(maximum([9,10,100]))