import xml.etree.ElementTree as ET

data = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

tree = ET.fromstring(data)
user_list = tree.findall('users/user')
print(len(user_list))
#print('Name: ')

for word in user_list:
    print('Name: ', word.find('name').text)