Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1=('physics','chemistry','1997','2000')
>>> tup1[0]
'physics'
>>> tup1[0:2]
('physics', 'chemistry')
>>> tup1[2]=2001

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup1[2]=2001
TypeError: 'tuple' object does not support item assignment
>>> tup2=('123','456','789')
>>> tup3=tup1+tup2
>>> tup3
('physics', 'chemistry', '1997', '2000', '123', '456', '789')
>>> del tup1[0]

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del tup1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> cmp(tup1,tup2)
1
>>> max(tup1)
'physics'
>>> max(tup2)
'789'
>>> 
