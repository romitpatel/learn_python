import urllib.request
import twurl
import urllib.error
import ssl
import sqlite3
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqllite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Twitter (name TEXT,retrieved INTEGER,friends INTEGER)''')

# Ignore certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    accnt = input('Please enter username or quit:')
    if accnt=='quit': break
    if (len(accnt) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            accnt = cur.fetchone()[0]
        except:
            print('No retrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL,{'screenname': accnt, 'count': '20'})
    print('Retrieving: ',url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining',headers['x-rate-limit-remaining'])
    js = json.loads(data)

    print(json.dumps(js,indent=2))

    cur.execute('UPDATE Twitter SET retrieved = 1 WHERE name = ?', (accnt, ))
    count_new = 0
    count_old = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',(friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friend = ? WHERE name = ?', (count+1, friend))
            count_old = count_old + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES (?,0,1)''', (friend, ))
            count_new = count_new + 1
    print('New accounts=', count_new,'revisited=',count_old)
    conn.commit()



cur.close()

