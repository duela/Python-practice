# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 20:03:51 2022

@author: yinku
"""

import sqlite3 

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute(''' CREATE TABLE Counts (org Text, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname)<1):fname = 'mbox.txt'
fh = open(fname)
for line in fh: 
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(email,))
conn.commit()     # commit every 10 or 20 records etc
    
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print((row[0],row[1]))
cur.close()
#"emaildb.py" 34L, 942C written

import sqlite3

conn = sqlite3.connect('ass.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    parts = email.split('@')
    org = parts[-1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (org, ))
    #conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()