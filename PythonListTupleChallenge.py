Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Challenge Day 19
>>> firstlist = [1,2,3,4,5,6,7,8,9] * 3
>>> print(len(firstlist))
27
>>> print(firstlist)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> firstlist.append(10)
>>> for x in firstlist:
	print(x)

	
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
10
>>> secondlist = firstlist.copy()
>>> print(len(secondlist))
28
>>> thirdlist = secondlist.copy([0:10])
SyntaxError: invalid syntax
>>> thirdlist = secondlist[0:10]
>>> print(thirdlist)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
>>> for x in firstlist:
	if x == 4
	
SyntaxError: invalid syntax
>>> for x in firstlist:
	if x == 4:
		firstlist.remove(x)

		
>>> for x in firstlist:
	print(x)

	
1
2
3
5
6
7
8
9
1
2
3
5
6
7
8
9
1
2
3
5
6
7
8
9
10
>>> firstlist.sort()
>>> for x in firstlist:
	print(x)

	
1
1
1
2
2
2
3
3
3
5
5
5
6
6
6
7
7
7
8
8
8
9
9
9
10
>>> firstlist.reverse()
>>> for x in firstlist:
	print(x)

	
10
9
9
9
8
8
8
7
7
7
6
6
6
5
5
5
3
3
3
2
2
2
1
1
1
>>> firstlist.pop(0)
10
>>> firstlist.insert(0, 11)
>>> for x in firstlist:
	print(x)

	
11
9
9
9
8
8
8
7
7
7
6
6
6
5
5
5
3
3
3
2
2
2
1
1
1
>>> firstlist.count(1)
3
>>> for n in thirdlist:
	print(n)

	
1
2
3
4
5
6
7
8
9
1
>>> thirdlist.reverse()
>>> for n in thirdlist:
	print(n)

	
1
9
8
7
6
5
4
3
2
1
>>> thirdlist.sort()
>>> for n in thirdlist:
	print(n)

	
1
1
2
3
4
5
6
7
8
9
>>> seconlist.clear()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    seconlist.clear()
NameError: name 'seconlist' is not defined
>>> secondlist.clear()
>>> thirdlist.extend((10,20,30,40,50,60,70,80,90))
>>> for n in thirdlist:
	print(n)

	
1
1
2
3
4
5
6
7
8
9
10
20
30
40
50
60
70
80
90
>>> newtuple = ("java","python","swift")
>>> platform = ("Node", "Angular","React")
>>> platform += newtuple
>>> for x in platform:
	print(x)

	
Node
Angular
React
java
python
swift
>>> platform.index("React")
2
>>> 
