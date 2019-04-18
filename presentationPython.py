# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:02:45 2019

@author: Dell
"""

i = input('Enter ')
i=int(i)
if i == 1:
    print('1')
elif i ==2:
    print('2')
else:
    print('!1!2')

string = 'my string'
for z in string:
    print(z)

#decorators
def fun1(fun2):
    print('------')
    fun2()
    print('------')

@fun1
def fun2():
    print('Hello')
    
class A:
    dec = 10
    def prt():
        print('hello')
        
num=A
print(num.dec)
num.prt

