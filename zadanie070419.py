# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:46:09 2019

@author: Dell
"""

#1
def nichego():
    pass
#2
def umn2(a,b):
    return a*b

print(umn2(2,4))
#3
def checkTchetnost(a):
    if a%2 == 0:
        z='yes'
    else:
        z='no'
    return print(z)

checkTchetnost(2)

#4
def fun4(a,b):
    if a>10:
        print('да')
    else:
        print('нет')
        
fun4(19,6)

#5
f = lambda a,b:a%b
print(f(3,2))

#6

def mydec(g):
    def u():
        print("Dear",g())
    return u()

@mydec
def g():
    return 'Ivan'

#7

def maximize(alfa):
    return alfa*alfa

beta = [1,2,3,4,5]
beta = list(map(maximize,beta))
print(beta)

def checking(s):
    return s > 9

beta = list(filter(checking,beta))
print(beta)
    
#8

a=1
def f1():
    global a
    a=2
    
def f2():
    a=1
    a+=3
    
f2() 
print(a)
f1()
print(a) 

#9

def minmax(spis):
    print('min ',min(spis))
    print('max ',max(spis))
    
minmax([5,1,4,56,3,100,13,45,56,78])

#10
def visokosnii(year):
    if year%100 !=0:
        if year%4 == 0:
            return True
        else:
            return False
    else:
        return False
yr=int(input('Введите год:'))
print(yr,'',visokosnii(yr))

#11
def season(month):
    if month == 12 or month == 1 or month == 2:
        return 'Winter'
    
    if month == 3 or month == 4 or month == 5:
        return 'Spring'
    
    if month == 6 or month == 7 or month == 8:
        return 'Summer'
    
    if month == 9 or month == 10 or month == 11:
        return 'Autumn'
    
print(season(11))    

#12
calendar = ['1.2.2019','13.4.2019','7.4.2019']
def date(day,month,year):
    date_for_checking = str(str(day) + '.' +str(month) + '.' + str(year))
    for i in  calendar:
        if i ==  date_for_checking:
            return True
       
    return False
    #print(date_for_checking)

print(date(int(input('Введите день:')),int(input('Введите месяц: ')),int(input('Введите год:'))))

#13

spisok = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD'] 

def last(spis):
    res=[]
    for i in spis:
        if type(i) == int or type(i) == float:
            res.append(i)
    
    res = sorted(res)
    return res

print(last(spisok))


'''
1) Создадим пустую функцию которая ничего не возвращает.
2) Написать функцию, которая принимает число, возвращает его значение умноженное на два.
3) Напишем функцию, которая определяет параметр на чётность. Если чётное число принтим (‘yes’) в ином случае (‘no’).
4) Пишем функцию, принимающую два аргумента. После чего проверим, если первое число больше 10, принтим (‘да’). Если меньше(‘нет’).
5) Написать лямбда функцию, которая делит по модулю(%) два аргумента.
6) Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции.
7) Использовать функцию map и filter 
8) Создадим чистую и нечистую функцию.
9) Сделать функцию поиска минимума и максимума в списке.
10) Написать функцию, которая определяет, является ли год високосным. Пользователь вводит год, если он високосный, то функция возвращает True. Если нет, то False.
11)
ddddddddddddddddddddddddd
'''