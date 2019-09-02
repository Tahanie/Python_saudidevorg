Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python Day#14
>>> list = ["a","b","c","d","e","f","g","h"]
>>> print(len(list))
8
>>> print(list[3:6])
['d', 'e', 'f']
>>> if D in list:
	print("Yes, it is in the List")

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    if D in list:
NameError: name 'D' is not defined
>>> if "D" in list:
	print("Yes, it is in the List")

	
>>> newlist = ["بايثون بالعربية"] * 5
>>> print(len(newlist))
5
>>> print(newlist)
['بايثون بالعربية', 'بايثون بالعربية', 'بايثون بالعربية', 'بايثون بالعربية', 'بايثون بالعربية']
>>> secondlist = ["Python everywhere"]
>>> newlist += secondlist
>>> print(newlist)
['بايثون بالعربية', 'بايثون بالعربية', 'بايثون بالعربية', 'بايثون بالعربية', 'بايثون بالعربية', 'Python everywhere']
>>> if secondlist in newlist:
	print("True")

	
>>> if "Python everywhere" in newlist:
	print("True")

	
True
>>> if "D" not in list:
	a = ["D"]
	list += a

	
>>> print(len(list))
9
>>> print(list)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'D']
>>> if "Hi" not in list:
	b=["Hi"] * 5
	list += b

	
>>> print(list)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'D', 'Hi', 'Hi', 'Hi', 'Hi', 'Hi']
>>> print(a)
['D']
>>> print(b)
['Hi', 'Hi', 'Hi', 'Hi', 'Hi']
>>> 
