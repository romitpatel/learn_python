import sqlite3

conn = sqlite3.connect('music.sqllite3')
curs = conn.cursor()

curs.execute('DROP TABLE IF EXISTS Tracks')
curs.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()