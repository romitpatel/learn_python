import urllib.request

info = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('new_img1.jpg','wb')

size = 0
while True:
    img = info.read(100000)
    if len(img)<1:break
    size = size + len(img)
    fhand.write(img)

print('characters copied',size)
fhand.close()

