def fun(a,b=2):
    try:
        print(a/b)
    except:
        print('divide by zero')

fun(3)

def plusone(a):
    return a+1


def check(z):
    return z>5

print(plusone(3))

# map and filter
l=[5,6,7]
l = list(map(plusone,l))
print (l)

l = list(filter(check,l))
print (l)

#декор

def decorator(fin):
    def walpaper():
        print('==========')
        fin()
        print('==========')
    return walpaper()

@decorator
def fin():
    print('hello')
    
#  переменные локальные и глобальные
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

#lambda

f = lambda x,y,z:x+y+z
print(f(1,2,3))

