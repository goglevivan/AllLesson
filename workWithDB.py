# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:01:56 2019

@author: Dell
"""

import sqlite3
con = sqlite3.connect('D:/DB/TestDB.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS test(id int PRIMARY KEY,name  varchar(50))')

cur.execute("INSERT INTO test VALUES(1,'ivan')")
cur.execute("INSERT INTO test VALUES(2,'igor')")


sql ="""select id,name from test
Where test.name = "
"""
zap  = str(input('Введите имя которые надо вывести:'))

cur.execute(sql + zap + '";')
"""
try:
    
except:
    print("ERORR")
"""
#zap  = str(input('Введите имя которые надо вывести:'))

#cur.execute('SELECT * FROM test WHERE name = '+zap+';')
#cur.execute('SELECT * FROM test ;')
res = cur.fetchall()
print (res)
'''if res != []:
    print(res)'''
con.commit()
cur.close()
con.close()