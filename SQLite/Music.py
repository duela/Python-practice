# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 22:51:52 2022

@author: yinku
"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.execute('''DROP TABLE IF EXIST Artist;
            DROP TABLE IF EXIST Album;
            DROP TABLE IF EXIST Track;  
            ''')
cur.execute(''' CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
                   
            CREATE TABLE "Album" (
	"id"	INTEGER NOT NULL UNIQUE,
	"artist_id"	INTEGER,
	"title"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
            CREATE TABLE "Track" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"album_id"	INTEGER,
	"genre_id"	INTEGER,
	"len"	INTEGER,
	"rating"	INTEGER,
	"count"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
            ''')
fname = "Library.xml"
if (len(fname) < 1): fname = "Library.xml"

def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text 
        if child.tag == 'key' and child.text == key:
            found = True
        return None
    

