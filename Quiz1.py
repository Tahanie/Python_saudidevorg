Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Quiz
>>> str = "Please, I want {} sandowishes and {} donutes"
>>> sandno= 5
>>> donuno = 7
>>> print(str.replace("i","we"))
Please, I want {} sandowweshes and {} donutes
>>> print(str.replace("I","We"))
Please, We want {} sandowishes and {} donutes
>>> newstr = str.replace("I","We")
>>> print(newstr.format(sandno,donuno))
Please, We want 5 sandowishes and 7 donutes
>>> print(newstr.replace("a","A"))
PleAse, We wAnt {} sAndowishes And {} donutes
>>> acapital = newstr.find("A",0,len(newstr))
>>> print(acapital)
-1
>>> acapital = newstr.find("a",0,len(newstr))
>>> acapital = newstr.find("A",0,len(newstr))
>>> acapital = newstr.find("a",0,len(newstr))
>>> print(acapital)
3
>>> acapital = newstr.replace("a","A")
>>> print(acapital)
PleAse, We wAnt {} sAndowishes And {} donutes
>>> print(acapital.format(sandno, donuno))
PleAse, We wAnt 5 sAndowishes And 7 donutes
>>> 
