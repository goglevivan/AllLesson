# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:48:08 2019

@author: Dell
"""
import math
####### 1 #######
class Apple:
    def __init__(self,color,size,year,price):
        self.color = color
        self.size = size
        self.year = year
        self.price = price

####### 2 ######
class Circle:  
    def area(r):
        return (r **2)*math.pi
       
    

b = Circle
print(b.area(12))

####### 3 #######
class Person:
    def __init__(self,name,surname,qual = 1):
        self.name = name
        self.qual = qual
        self.surname = surname
        
    def information(self):
        return (self.name ,self.surname ,self.qual)
    
man = Person('Иван','Иванов')
print(man.information())

####### 4 #######
class Triangle:
    def __init__(self,a,h):
        self.a = a
        self.h = h
        
    def area(self):
        return self.a * self.h / 2
tri = Triangle(5,3)
print('area is:',tri.area())

####### 5 #######

class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def calculate_perimetr(self):
        return (self.a + self.b)*2
    
class Square:
    def __init__(self,a):
        self.a = a
        
    
    def calculate_perimetr(self):
        return (self.a * 2 )*2

r = Rectangle(2,3)
s = Square(4)
print('Rectangle',r.calculate_perimetr())
print('Square',s.calculate_perimetr())

####### 6 #######
class Square:
    def __init__(self,a):
        self.a = a
        
    
    def calculate_perimetr(self):
        return (self.a * 2 )*2
    
    def change_size(self,z):
        self.a = self.a + z
        
s = Square(4)
s.change_size(-4)
print('Square',s.calculate_perimetr())
     