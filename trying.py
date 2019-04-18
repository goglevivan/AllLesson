# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:40:30 2019

@author: Dell
"""
import requests
a=int(input())

b=int(input())
try:
    z = a/b
    print(z)
except ZeroDivisionError:
    print(a)
finally:
    print("Write ")
url_my_404 ='www.ivgo180419.com'
print(requests.get(url_my_404))