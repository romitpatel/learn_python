txt = 'I am going to use the dsu method to decorate, sort and undecorate this piece of text.'
words = txt.split()
print(words)


decorate_list = list()
for word in words:
    decorate_list.append((len(word), word))

# sort the list
print(decorate_list)
decorate_list.sort(reverse=True)
print(decorate_list)

# undecorate the list

undecorate_list = list()

for length, word in decorate_list:
    undecorate_list.append(word)

print(undecorate_list)