import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]
'''

info = json.loads(data)

for item in info:
    print('name',item['name'])
    print('id', item['id'])
    print('x', item['x'])