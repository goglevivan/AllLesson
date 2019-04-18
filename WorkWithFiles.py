# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:22:57 2019

@author: Dell
"""
### Wrok with open command ###
st = open("kek.txt","w")
st.write("Example")
st.close()

### with ###

with open("kek.txt","w") as f:
    f.write("Test")
    
### Reading ###
with open("kek.txt","r") as f:
    print(f.read())
##Try##
a=input()
a=int(a)
b=input()
b=int(a)
z = a/b
print(z)