Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [10,20,30,'forty',True,[12,23,34,45,56],10.7,12.8,45.9]
>>> list1
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8, 45.9]
>>> list1[5][0]
12
>>> list1[5][-1]
56
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> del list1
>>> list1 = [10,20,30,'forty',True,[12,23,34,45,56],10.7,12.8,45.9]
>>> list1.clear()
>>> list1
[]
>>> id(list1)
4329130056
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> 
>>> list1 = [10,20,30,'forty',True,[12,23,34,45,56],10.7,12.8,45.9]
>>> list2 = list1
>>> list1
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8, 45.9]
>>> list2
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8, 45.9]
>>> list3 = list1.copy()
>>> list3
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8, 45.9]
>>> id(list1)
4329130056
>>> id(list2)
4329130056
>>> id(list3)
4364394824
>>> 
>>> del list1[-1]
>>> list1
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8]
>>> list2
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8]
>>> list3
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8, 45.9]
>>> 
>>> list1
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8]
>>> list3
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8, 45.9]
>>> id(list1[5])
4329130376
>>> id(list3[5])
4329130376
>>> 
>>> id(list1[3])
4364254768
>>> id(list3[3])
4364254768
>>> del list1[3]
>>> list1
[10, 20, 30, True, [12, 23, 34, 45, 56], 10.7, 12.8]
>>> list3
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 56], 10.7, 12.8, 45.9]
>>> list1[4][-1] = 65
>>> list1
[10, 20, 30, True, [12, 23, 34, 45, 65], 10.7, 12.8]
>>> list3
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 65], 10.7, 12.8, 45.9]
>>> 
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> list1
[10, 20, 30, True, [12, 23, 34, 45, 65], 10.7, 12.8]
>>> list3
[10, 20, 30, 'forty', True, [12, 23, 34, 45, 65], 10.7, 12.8, 45.9]
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65], 10.7, 12.8]
>>> list1[4][0] = 21
>>> list1
[10, 20, 30, True, [21, 23, 34, 45, 65], 10.7, 12.8]
>>> list3
[10, 20, 30, 'forty', True, [21, 23, 34, 45, 65], 10.7, 12.8, 45.9]
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65], 10.7, 12.8]
>>> 
>>> list4.append(1)
>>> list4.append(0)
>>> list4.append(False)
>>> list4.append('forty')
>>> list4[4].append(10)
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65, 10], 10.7, 12.8, 1, 0, False, 'forty']
>>> list4.count( 10 )
1
>>> list4.count( 1 )
2
>>> int(True)
1
>>> int(False)
0
>>> list4.count( 0 )
2
>>> list4.count( True )
2
>>> list4.index( 1 )
3
>>> list4.index( 1, 4 )
7
>>> list4[7]
1
>>> list4.insert( 5, 100 )
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65, 10], 100, 10.7, 12.8, 1, 0, False, 'forty']
>>> list4[5] = 100
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65, 10], 100, 10.7, 12.8, 1, 0, False, 'forty']
>>> list4[5] = 200
>>> list4.insert( 5, 300 )
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65, 10], 300, 200, 10.7, 12.8, 1, 0, False, 'forty']
>>> list4.insert( 5, 999 )
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65, 10], 999, 300, 200, 10.7, 12.8, 1, 0, False, 'forty']
>>> list4[5] = 0.1
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65, 10], 0.1, 300, 200, 10.7, 12.8, 1, 0, False, 'forty']
>>> list4.pop()
'forty'
>>> list4.pop()
False
>>> list4.pop()
0
>>> list4.pop(5)
0.1
>>> list1
[10, 20, 30, True, [21, 23, 34, 45, 65], 10.7, 12.8]
>>> list4
[10, 20, 30, True, [12, 23, 34, 45, 65, 10], 300, 200, 10.7, 12.8, 1]
>>> 
>>> list4.remove(30)
>>> list4
[10, 20, True, [12, 23, 34, 45, 65, 10], 300, 200, 10.7, 12.8, 1]
>>> list4.remove(1)
>>> 
>>> list4
[10, 20, [12, 23, 34, 45, 65, 10], 300, 200, 10.7, 12.8, 1]
>>> list4.reverse()
>>> list4
[1, 12.8, 10.7, 200, 300, [12, 23, 34, 45, 65, 10], 20, 10]
>>> list4.sort()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list4.sort()
TypeError: '<' not supported between instances of 'list' and 'float'
>>> list4.pop( 5 )
[12, 23, 34, 45, 65, 10]
>>> list4
[1, 10.7, 12.8, 200, 300, 20, 10]
>>> list4.sort()
>>> list4
[1, 10, 10.7, 12.8, 20, 200, 300]
>>> list4.sort(reverse=True)
>>> list4
[300, 200, 20, 12.8, 10.7, 10, 1]
>>> list4.sort().reverse()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    list4.sort().reverse()
AttributeError: 'NoneType' object has no attribute 'reverse'
>>> list4.sort()
>>> 
>>> list4.reverse()
>>> list4
[300, 200, 20, 12.8, 10.7, 10, 1]
>>> tuple1 = [10,20,30,'forty',True,[12,23,34,45,56],10.7,12.8,45.9]
>>> del tuple1[0]
>>> tuple1 = (10,20,30,'forty',True,[12,23,34,45,56],10.7,12.8,45.9)
>>> type(tuple1)
<class 'tuple'>
>>> del tuple1[0]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> tuple1[0] = 100
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    tuple1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> dir(tuple1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> tuple1[5][0] = 100
>>> tuple1
(10, 20, 30, 'forty', True, [100, 23, 34, 45, 56], 10.7, 12.8, 45.9)
>>> tuple1[5] = [1,2,3]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    tuple1[5] = [1,2,3]
TypeError: 'tuple' object does not support item assignment
>>> 
