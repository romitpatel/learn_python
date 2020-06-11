def chop(t):
    del t[0]
    del t[len(t)-1]
    return None

list1 = [1,2,3,4]
print(chop(list1))
print(list1)

def middle(t):
    del t[1:len(t)-1]

list2 = [5,6,7,8,9,10]
middle(list2)
print(list2)
