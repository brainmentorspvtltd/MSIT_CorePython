Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # array vs list
>>> # int arr[] = [10,20,30]
>>> list1 = [ 10, 20, 30, 'forty', True, 50.5, [ 11, 12, 13, 14, 15 ] ]
>>> list1
[10, 20, 30, 'forty', True, 50.5, [11, 12, 13, 14, 15]]
>>> # list is a collection of elements having different data types
>>> list1[0]
10
>>> id(list1[0])
4538605008
>>> id(list1[1])
4538605328
>>> id(list1[2])
4538605648
>>> list1[-1]
[11, 12, 13, 14, 15]
>>> list1[-1][0]
11
>>> list1[2:5]
[30, 'forty', True]
>>> list1[2:]
[30, 'forty', True, 50.5, [11, 12, 13, 14, 15]]
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list1 = [ 10, 20, 30, 'forty', True, 50.5, [ 11, 12, 13, 14, 15 ] ]
>>> del list1[2]
>>> list1
[10, 20, 'forty', True, 50.5, [11, 12, 13, 14, 15]]
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list1.append(1000)
>>> list1
[10, 20, 'forty', True, 50.5, [11, 12, 13, 14, 15], 1000]
>>> list1.append( [123,234,345] )
>>> list1
[10, 20, 'forty', True, 50.5, [11, 12, 13, 14, 15], 1000, [123, 234, 345]]
>>> list1.extend( [123,234,345] )
>>> list1
[10, 20, 'forty', True, 50.5, [11, 12, 13, 14, 15], 1000, [123, 234, 345], 123, 234, 345]
>>> for i in range(11):
	print( list1[i] )

	
10
20
forty
True
50.5
[11, 12, 13, 14, 15]
1000
[123, 234, 345]
123
234
345
>>> del list1[-1]
>>> for i in range(11):
	print( list1[i] )

	
10
20
forty
True
50.5
[11, 12, 13, 14, 15]
1000
[123, 234, 345]
123
234
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    print( list1[i] )
IndexError: list index out of range
>>> len(list1)
10
>>> 
>>> for i in range( len( list1 ) ):
	print( list1[i] )

	
10
20
forty
True
50.5
[11, 12, 13, 14, 15]
1000
[123, 234, 345]
123
234
>>> list1.append("new data")
>>> list1
[10, 20, 'forty', True, 50.5, [11, 12, 13, 14, 15], 1000, [123, 234, 345], 123, 234, 'new data']
>>> list1.extend("python")
>>> list1
[10, 20, 'forty', True, 50.5, [11, 12, 13, 14, 15], 1000, [123, 234, 345], 123, 234, 'new data', 'p', 'y', 't', 'h', 'o', 'n']
>>> for i in range( len( list1 ) ):
	print( list1[i] )

	
10
20
forty
True
50.5
[11, 12, 13, 14, 15]
1000
[123, 234, 345]
123
234
new data
p
y
t
h
o
n
>>> 
