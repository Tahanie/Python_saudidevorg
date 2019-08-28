Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = """ This is a new lesson
in python to write in multiple lines"""
>>> print(a)
 This is a new lesson
in python to write in multiple lines
>>> arabic = "تجربة الكتابه بالعربي"
>>> print(arabic)
تجربة الكتابه بالعربي
>>> print(arabic[1])
ج
>>> a = "Hello, world"
>>> print(a[1])
e
>>> b = "Hello, world"
>>> print(b[2:5])
llo
>>> str = "Hello, world"
>>> print(str[0])
H
>>> print(str[1])
e
>>> print(str(len))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(str(len))
TypeError: 'str' object is not callable
>>> print(len(str))
12
>>> print(str[5,11])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(str[5,11])
TypeError: string indices must be integers
>>> print(str[5:11])
, worl
>>> print(str[5,12])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(str[5,12])
TypeError: string indices must be integers
>>> print(str[5:12])
, world
>>> str = " Hello, World! "
>>> print(str.strip()) #remove the space
Hello, World!
>>> print(len(str))
15
>>> print(Len(str.strip()))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(Len(str.strip()))
NameError: name 'Len' is not defined
>>> print(len(str.strip()))
13
>>> a = " HELLOW, WORLD! "
>>> print(lower(a.strip()))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(lower(a.strip()))
NameError: name 'lower' is not defined
>>> print((a.strip().lower()))
hellow, world!
>>> b = "HELLO, WORLD"
>>> print(b.lower())
hello, world
>>> print(b.upper())
HELLO, WORLD
>>> arabic = "العربية"
>>> print(arabic.lower())
العربية
>>> print(arabic.upper())
العربية
>>> print(arabic.replace("ة","ه"))
العربيه
>>> a = "Hello, world"
>>> print(a.replace("o","ت"))
Hellت, wتrld
>>> print(a.split(","))
['Hello', ' world']
>>> print(a.split("o"))
['Hell', ', w', 'rld']
>>> print(a.split("l"))
['He', '', 'o, wor', 'd']
>>> 
