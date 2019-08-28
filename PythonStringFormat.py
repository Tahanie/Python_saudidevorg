Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> age = 36
>>> txt = "My name is Johan, I am " + str(age)
>>> print (txt)
My name is Johan, I am 36
>>> txt = "My name is John, I am {}"
>>> print(txt.format(age))
My name is John, I am 36
>>> quantity = 3
>>> itemno = 567
>>> price = 49.95
>>> myorder ="I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity,itemno, price))
I want 3 pieces of item 567 for 49.95 dollars.
>>> myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
>>> print(myorder.format(quantity, itemno, price))
I want to pay 49.95 dollars for 3 pieces of item 567.
>>> firstname = "John"
>>> lastname = "Ann"
>>> fullname =""
>>> fullname = "{0} {1}"
>>> print(fullname.format(firstname,lastname))
John Ann
>>> 
