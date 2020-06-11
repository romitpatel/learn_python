str = 'hello 123, 566, wor890, there'
import re
x = re.findall('([0-9])',str)
print(x)
['3', '6', '0']
