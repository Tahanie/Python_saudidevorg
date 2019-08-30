Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> print ( x <3 or x < 4)
False
>>> x = ["apple", "banana"]
>>> y = ["apple", "banana"]
>>> z = x
>>> print (x is y)
False
>>> print ( x is z)
True
>>> print ( x is not y)
True
>>> print ( x is not z)
False
>>> print ( x != y)
False
>>> print ( x == y)
True
>>> print("apple" in x)
True
>>> print("banana" not in x)
False
>>> #Python Bitwise Operators
>>> a = 60
>>> b = 13
>>> c = 0
>>> c = a & b
>>> print (" C Value is " + str(c))
 C Value is 12
>>> c = a | b
>>> print ("C Value is " +str(c))
C Value is 61
>>> c = a ^ b
>>> print ("C Value is " +str(c))
C Value is 49
>>> c = ~a
>>> print ("C Value is " +str(c))
C Value is -61
>>> c = a <<< 2
SyntaxError: invalid syntax
>>> c = a << 2
>>> print ("C Value is " +str(c))
C Value is 240
>>> c = a >> 2
>>> print ("C Value is " +str(c))
C Value is 15
>>> 
