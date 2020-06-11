import sqlite3

conn = sqlite3.connect('music.sqllite3')
curs = conn.cursor()

curs.execute('INSERT INTO Tracks (title,plays) VALUES (?,?)',('Thunderstruck',20))
curs.execute('INSERT INTO Tracks (title,plays) VALUES (?,?)',('My Way',15))

conn.commit()

print('Tracks: ')
curs.execute('SELECT title, plays FROM Tracks')
for row in curs:
    print(row)

curs.execute('DELETE FROM Tracks where plays<100')
conn.commit()

conn.close()
