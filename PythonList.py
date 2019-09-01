Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python List
>>> s = []
>>> print(s)
[]
>>> print(type(s))
<class 'list'>
>>> numbers = [1,2,3,4,5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>>  fruitList =["banana","Apple","cherry"]
 
SyntaxError: unexpected indent
>>> fruitlist = ["banana","Apple","Cherry"]
>>> print(fruitlist)
['banana', 'Apple', 'Cherry']
>>> complist = ["banana","apple","cherry",1,2,3]
>>> print(complist)
['banana', 'apple', 'cherry', 1, 2, 3]
>>> decimallist = [0.2,0.5,1.2,4.8]
>>> print(decimallist)
[0.2, 0.5, 1.2, 4.8]
>>> orlist = [1,2,3,4,5,6,7,8,9]
>>> newlist = [float(n) for n in orlist]
>>> print(newlist)
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
>>> print(newlist[1])
2.0
>>> print(newlist[0])
1.0
>>> for x in new list:
	
SyntaxError: invalid syntax
>>> for x in newlist
SyntaxError: invalid syntax
>>> for x in newlist:
	print(x)

	
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
>>> complist [5] = 3.0
>>> print(complist)
['banana', 'apple', 'cherry', 1, 2, 3.0]
>>> for c in complist:
	print(c)

	
banana
apple
cherry
1
2
3.0
>>> complist[6]= 'test'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complist[6]= 'test'
IndexError: list assignment index out of range
>>> del complist[4]
>>> print(complist)
['banana', 'apple', 'cherry', 1, 3.0]
>>> del complist[0]
>>> print(complist[1])
cherry
>>> for c in complist:
	print(c)

	
apple
cherry
1
3.0
>>> 
