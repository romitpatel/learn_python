"""
split()
find()
upper()
lower()
capitalize()
startswith()
uppercase letters come before lowercase
"""
word = 'banana'
new_word = word.upper()
print(new_word)

i = word.find('b')
print(i)

i = word.find('na')
print(i)

i = word.find('na',3)
print(i)

word = ' hello how are you   '
new_word = word.strip()
print(new_word)

str = 'X-DSPAM-Confidence:0.8475'
index = str.find(':')
print(index)

str1 = str[index+1:]
print(float(str1))

