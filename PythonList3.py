Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python List 3 Day#15
>>> list = ["a","b","c","d"]
>>> print(len(list))
4
>>> list.append("e")
>>> print(list)
['a', 'b', 'c', 'd', 'e']
>>> list.insert(1,"A")
>>> print(list)
['a', 'A', 'b', 'c', 'd', 'e']
>>> list.remove("b")
>>> print(list)
['a', 'A', 'c', 'd', 'e']
>>> newlist = ["a"] * 5
>>> print(newlist)
['a', 'a', 'a', 'a', 'a']
>>> newlist.remove("a")
>>> print(newlist)
['a', 'a', 'a', 'a']
>>> newlist.remove("b")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    newlist.remove("b")
ValueError: list.remove(x): x not in list
>>> newlist.remove("a")
>>> newlist.remove("a")
>>> newlist.remove("a")
>>> newlist.remove("a")
>>> print(newlist)
[]
>>> newlist.remove("a")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    newlist.remove("a")
ValueError: list.remove(x): x not in list
>>> newlist += ["a","b","a","c","d"]
>>> print(len(newlist))
5
>>> newlist.pop()
'd'
>>> print(newlist)
['a', 'b', 'a', 'c']
>>> newlist.pop(2)
'a'
>>> print(newlist)
['a', 'b', 'c']
>>> newlist.clear()
>>> print(newlist)
[]
>>> firstlist = [1,2,3,4,5]
>>> secondlist = firstlist.copy()
>>> print(secondlist)
[1, 2, 3, 4, 5]
>>> thirdlist += firstlist
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    thirdlist += firstlist
NameError: name 'thirdlist' is not defined
>>> thirdlist =[]
>>> thirdlist += firstlist
>>> print(thirdlist)
[1, 2, 3, 4, 5]
>>> templist = firstlist
>>> print(templist)
[1, 2, 3, 4, 5]
>>> firstlist.pop()
5
>>> print(templist)
[1, 2, 3, 4]
>>> thislist = ["apple","banana","cherry"]
>>> mylist = list(thislist)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    mylist = list(thislist)
TypeError: 'list' object is not callable
>>> mylist = []
>>> mylist = list(thislist)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    mylist = list(thislist)
TypeError: 'list' object is not callable
>>> mylist = list(("apple","banana","cherry"))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    mylist = list(("apple","banana","cherry"))
TypeError: 'list' object is not callable
>>> intlist = [1,2,3,4,5]
>>> myrange = list(range(1,10))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    myrange = list(range(1,10))
TypeError: 'list' object is not callable
>>> intlist.reverse()
>>> print(intlist)
[5, 4, 3, 2, 1]
>>> intlist.sort()
>>> print(intlist)
[1, 2, 3, 4, 5]
>>> 
