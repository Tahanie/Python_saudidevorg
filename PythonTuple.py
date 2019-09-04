Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python Tuple Day 16
>>> newtuple = ("apple", "banana", "orange")
>>> print(newtuple)
('apple', 'banana', 'orange')
>>> print(len(newtuple))
3
>>> onlytuple =("a",)
>>> print(onlytuple)
('a',)
>>> print(len(onlytuple))
1
>>> print(type(onlytuple))
<class 'tuple'>
>>> Istuple = ("a")
>>> print(type(Istuple))
<class 'str'>
>>> secondtuple = (1.0, 2.5, "tuple", 'بايثون')
>>> print(secondtuple)
(1.0, 2.5, 'tuple', 'بايثون')
>>> print(secondtuple[2])
tuple
>>> secondtuple[1] = 3.5
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    secondtuple[1] = 3.5
TypeError: 'tuple' object does not support item assignment
>>> for x in secondtuple:
	print(x)

	
1.0
2.5
tuple
بايثون
>>> newtuple[3]='cherry'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    newtuple[3]='cherry'
TypeError: 'tuple' object does not support item assignment
>>> print(newtuple)
('apple', 'banana', 'orange')
>>> del newtuple
>>> print(newtuple)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(newtuple)
NameError: name 'newtuple' is not defined
>>> print(secondtuple [0:3])
(1.0, 2.5, 'tuple')
>>> newtuple = secondtuple
>>> print(newtuple)
(1.0, 2.5, 'tuple', 'بايثون')
>>> thirdtuple = newtuple [0:3]
>>> print(thirdtuple)
(1.0, 2.5, 'tuple')
>>> for x in thirdtuple:
	if x is not in newtuple:
		
SyntaxError: invalid syntax
>>> for x in thirdtuple:
	if x not in newtuple:
		print(x)

		
>>> for x in newtuple:
	if x not in thirdtuple:
		print(x)

		
بايثون
>>> 
