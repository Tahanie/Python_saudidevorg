Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Paython Casting
>>> x = int(1)
>>> y = int(2.6)
>>> z = int("3")
>>> n = int(1.2)
>>> print(x)
1
>>> print(y)
2
>>> print(z)
3
>>> print(n)
1
>>> x = float(1)
>>> y = float(2.8)
>>> z = float("4")
>>> n = float(3.1)
>>> print(x)
1.0
>>> print(y)
2.8
>>> print(z)
4.0
>>> print(n)
3.1
>>> x = str("s1")
>>> y = str(2)
>>> z = str(3.0)
>>> print(x)
s1
>>> print(y)
2
>>> print(z)
3.0
>>> print(type(x))
<class 'str'>
>>> print(type(y))
<class 'str'>
>>> x = int("s1")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x = int("s1")
ValueError: invalid literal for int() with base 10: 's1'
>>> 
