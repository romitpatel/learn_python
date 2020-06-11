word = 'brontosaurus'

d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

d2 = dict()
for c in word:
    d2[c] = d2.get(c,0)+1



print(d)