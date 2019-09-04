Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python tuple 2 Day 17
>>> newtuple = ("apple", "banana","cherry")
>>> if "orange" in newtuple:
	print("Yes")

	
>>> newtuple.clear()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    newtuple.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> del newtuple
>>> fruiTuple = ("apple", "banana","cherry")
>>> if "apple" in fruiTuple:
	print("Yes")

	
Yes
>>> newtuple = ('Hi',) *3
>>> print(newtuple)
('Hi', 'Hi', 'Hi')
>>> temtuple = ('hello') * 2
>>> print(temtuple)
hellohello
>>> intTuple = (5) * 5
>>> print(intTuple)
25
>>> del intTuple
>>> intTuple = (5,) * 5
>>>  print(intTuple)
 
SyntaxError: unexpected indent
>>> print(intTuple)
(5, 5, 5, 5, 5)
>>> intTuple += (1,2,3)
>>> print(intTuple)
(5, 5, 5, 5, 5, 1, 2, 3)
>>> print(len(intTuple))
8
>>> numTuple ((1,3), (3,4), (4,2), (1,4))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    numTuple ((1,3), (3,4), (4,2), (1,4))
NameError: name 'numTuple' is not defined
>>> mergeTuple = tuple(("apple","banana", "cherry"))
>>> print(mergeTuple)
('apple', 'banana', 'cherry')
>>> mergeTuple = tuple(intTuple)
>>> print(mergeTuple)
(5, 5, 5, 5, 5, 1, 2, 3)
>>> thislist = [3,4,5,6, "A","B"]
>>> thisTuple = tuple(thislist)
>>> print(thisTuple)
(3, 4, 5, 6, 'A', 'B')
>>> print(thisTuple.count())
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(thisTuple.count())
TypeError: count() takes exactly one argument (0 given)
>>> print(intTuple.count(5))
5
>>> print(fruiTuple.index("banana"))
1
>>> if "cherry" in fruiTuple:
	print("Yes in index" + fruiTuple.index('cherry'))

	
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    print("Yes in index" + fruiTuple.index('cherry'))
TypeError: can only concatenate str (not "int") to str
>>> if "cherry" in fruiTuple:
	print("Yes in index" + str(fruiTuple.index('cherry')))

	
Yes in index2
>>> if "apple" in fruiTuple:
	print("Yes in index " + fruiTuple.index('apple'))

	
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    print("Yes in index " + fruiTuple.index('apple'))
TypeError: can only concatenate str (not "int") to str
>>>  if "apple" in fruiTuple:
	print("Yes in index " + str(fruiTuple.index('apple')))
	
SyntaxError: unexpected indent
>>> if "apple" in fruiTuple:
	print("Yes in index " +str(fruiTuple.index("apple")))

	
Yes in index 0
>>> 
