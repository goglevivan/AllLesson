# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:10:05 2019

@author: Dell
"""

import sqlite3
con = sqlite3.connect('D:/DB/TestDB.db')
cur = con.cursor()
zap  = str(input('Введите имя которое надо вывести:'))
cur.execute('select * from test2 WHERE name ="'+zap+'";')
res = cur.fetchall()
print (res)
con.commit()
cur.close()
con.close()