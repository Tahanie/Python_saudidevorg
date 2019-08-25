Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python Variables
>>> x = 5
>>> y ="John"
>>> print(x) print(y)
SyntaxError: invalid syntax
>>> print(x)
5
>>> print(y)
John
>>> x = 4
>>> x="Sally"
>>> print(x)
Sally
>>> x,y,z = "Orange","Banana","Cherry"
>>> print(x)
Orange
>>> print(y)
Banana
>>> print(z)
Cherry
>>> x = y = z ="Orange"
>>> print(x)
Orange
>>> print(y)
Orange
>>> print(z)
Orange
>>> x = "awesome"
>>> print ("Python is " + x)
Python is awesome
>>> x = "Python is "
>>> y = "awesome"
>>> z = x + y
>>> print (z)
Python is awesome
>>> x = 5
>>> y = 10
>>> print ( x+y)
15
>>> x = 5
>>> y = "John"
>>> print (x+y)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print (x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> x= "5"
>>> y= "Version"
>>> print (y+x)
Version5
>>> 
