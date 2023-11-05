# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:22:01 2022

@author: yinku
"""

from urllib.request import urlopen 
import urllib.error 
import twurl 
import json
import sqlite3 
import ssl


Twitter_url = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGERS) ''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

while True:
    account = input('Enter a Twitter account, or quit: ')
    if (account == 'quit'): break
    if (len(account)<1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            account = cur.fetchone()[0]    # sub zero is the first of the name (fetchone) means get one row from the database  [0] the first column from the database                         
        except:
            print('No retrieved Twitter accounts found')
            continue
        url = twurl.argument(Twitter_url, {'screen_name': account, 'count': '5'})
        print('Retrieving', url)
        connection = urlopen(url, context = ctx)
        data = connection.read().decode()
        headers = dict(connection.getheaders())
        print('REmaining', headers['x-rate-limit-remaining'])
        js = json.loads(data)   # pass list of data gotten  from twitter into json
        # print(json.dumps(js, indemt=4))
        
        cur.execute('UPDATE Twitter SET retrieved=1 WHERE name =?', (account,) )  # Update what was retrieved from 0 to 1
        countnew = 0
        countold = 0
        
        for i in js['users']:    # go through the users and print the screen name out
            friend = i['screen_name']
            print(friend)
            cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend,))
            
            try:
                count = cur.fetchone()[0]
                cur.execute('UPDATE Twitter SET friends=? WHERE name =?', (count+1,friend))
                countold = countold + 1
            except:
                cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES(?,0,1)''',(friend,))
                countnew = countnew + 1
        print('New accounts=', countnew, 'revisited= ', countold )
        #conn.commit()
    cur.close()
             
            
            
        
        
        
        