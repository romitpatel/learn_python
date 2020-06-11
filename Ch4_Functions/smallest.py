def minimum(values):
    small = None
    for value in values:
        if small is None or value < small:
            small = value
    return small

print(minimum([2,4,8]))

