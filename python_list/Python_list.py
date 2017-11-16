Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,3]
>>> list2 = [2,3,3]
>>> list * 2

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list * 2
TypeError: unsupported operand type(s) for *: 'type' and 'int'
>>> list1 *2
[1, 2, 3, 1, 2, 3]
>>> list2 *2
[2, 3, 3, 2, 3, 3]
>>> print type(list)
<type 'type'>
>>> print type (list1)
<type 'list'>
>>> var = 1
>>> print type (var)
<type 'int'>
>>> print "µØ"£¬var£¬Ò²
SyntaxError: invalid syntax
>>> print  "di",var , "ye "
di 1 ye 
>>> print "di "+var+"ye "

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print "di "+var+"ye "
TypeError: cannot concatenate 'str' and 'int' objects
>>> print "di "+str(var)+"ye"
di 1ye
>>> import random
>>> random.choice(['a','b','c'])
'c'
>>> random.choice('a','b','c')

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    random.choice('a','b','c')
TypeError: choice() takes exactly 2 arguments (4 given)
>>> random.choice(['a','b','c'])
'b'
>>> random.choice(['a','b','c'])
'b'
>>> random.choice(['a','b','c'])
'a'
>>> random.choice(['a','b','c'])
'b'
>>> random.choice(['a','b','c'])
'c'
>>> random.choice(['a','b','c'])
'a'
>>> 
>>> v

Traceback (most recent call last):v
  File "<pyshell#23>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> list1 = ['physics','chemistry',1997,2000]
>>> list1[0]
'physics'
>>> list1[1]
'chemistry'
>>> list1[2]
1997
>>> list1[3]
2000
>>> list1[0:3]
['physics', 'chemistry', 1997]
>>> list1[2]=20001
>>> list1
['physics', 'chemistry', 20001, 2000]
>>> list1[2]-4
19997
>>> list1
['physics', 'chemistry', 20001, 2000]
>>> list1[2]-=4
>>> lsit1

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    lsit1
NameError: name 'lsit1' is not defined
>>> list1
['physics', 'chemistry', 19997, 2000]
>>> list1[2]=1997
>>> list1
['physics', 'chemistry', 1997, 2000]
>>> list1.append('a')
>>> list1
['physics', 'chemistry', 1997, 2000, 'a']
>>> list1.append("b")
>>> list1
['physics', 'chemistry', 1997, 2000, 'a', 'b']
>>> list1[2]=1998
>>> list1
['physics', 'chemistry', 1998, 2000, 'a', 'b']
>>> list1[2]-=1
>>> list1
['physics', 'chemistry', 1997, 2000, 'a', 'b']
>>> del list1[5]
>>> list1
['physics', 'chemistry', 1997, 2000, 'a']
>>> list2=[1,2,3]
>>> list3=[4,5,6]
>>> cmp(list1,list2)
1
>>> cmp(list2,list3)
-1
>>> list2,list3=list3,list2
>>> list2
[4, 5, 6]
>>> list3
[1, 2, 3]
>>> cmp(list2,list3)
1
>>> max(list3)
3
>>> min(list3)
1
>>> list2.reverse()
>>> list2
[6, 5, 4]
>>> 
