import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'

else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Logic to paste input location and create a valid url for requesting data
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = service_url + urllib.parse.urlencode(parms)

    # Logic to read retrieved data from the url
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('======Failure to retrieve data=======')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    lat = js['results'][0]['geometry']['location']['lat']
    lon = js['results'][0]['geometry']['location']['lng']

    print('lat', lat, 'lon', lon)
    location = js['results'][0]['formatted_address']
    print(location)

