Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 1
>>> y = 2.8
>>> z = 1j
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> x = 1
>>> y = 356522222222222278999888888888
>>> z = -23456778
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> x = 1.12334
>>> y = 1.0
>>> z = - 23.234
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x = 35e3
>>> y=12E4
>>> z = -87.7e100
>>> print(type(x))
<class 'float'>
>>> print(x)
35000.0
>>> print(type(y))
<class 'float'>
>>> print(y)
120000.0
>>> print(type(z))
<class 'float'>
>>> print(z)
-8.77e+101
>>> x = 3+5j
>>> y = 5j
>>> z = -5j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>> print(type(z))
<class 'complex'>
>>> print(x)
(3+5j)
>>> print(y)
5j
>>> print(z)
(-0-5j)
>>> x = 1
>>> y = 2.8
>>> z = 1j
>>> a = float(x) #Covert to float
>>> b = int(y) #Convert to int
>>> c = complex(x) #Convert to complex
>>> print(a)
1.0
>>> print(b)
2
>>> print(c)
(1+0j)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> import random
>>> print(random.randrange(1,10))
8
>>> print(random.randrange(1,10))
5
>>> print(random.randrange(1,10))
6
>>> print(random.randrange(1,10))
3
>>> x="apple"
>>> y="Orange"
>>> z="limon"
>>> basket = x +' '+y+' '+ z
>>> print(basket)
apple Orange limon
>>> 
