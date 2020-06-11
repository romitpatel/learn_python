import urllib.request, urllib.error, urllib.parse
import re
import ssl

'''
Ignore certificate related errors
'''
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''
Extract all the links from the web page
'''

url = input('Enter: ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'"(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())

