Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # lexicography
>>> 
>>> employee = {
	}
>>> employee
{}
>>> type(employee)
<class 'dict'>
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000
	"designation" : "Developer",
	
SyntaxError: invalid syntax
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT"
	}
>>> 
>>> employee['id']
101
>>> employee['name']
'Ram'
>>> del employee['department']
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer'}
>>> 
>>> employee['department']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    employee['department']
KeyError: 'department'
>>> 
>>> employee['department'] = "IT"
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'department': 'IT'}
>>> employee['department'] = "Finance"
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'department': 'Finance'}
>>> 
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact_1" : 1234,
	"contact_2" : 5677,
	"contact_3" : 7808
	}
>>> 
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact" : [124, 3446, 467, 57668]
	}
>>> 
>>> employee['contact']
[124, 3446, 467, 57668]
>>> employee['contact'][0]
124
>>> 
>>> student = {
	"id" : 201,
	"name" : "Jenny",
	"class" : 12,
	"stream" : "Non-medical",
	"marks" : {
		"english" : 95,
		"maths" : 64,
		"physics" : 70,
		"chemistry" : 80,
		"cs" : 90,
		"ped" : 30
		},
	"attendance" : 75
	}
>>> 
>>> student['id']
201
>>> student['marks']
{'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}
>>> student['marks']['cs']
90
>>> len( student )
6
>>> for i in range( len ( student ) ):
	print(i)

	
0
1
2
3
4
5
>>> for x in student:
	print(x)

	
id
name
class
stream
marks
attendance
>>> student
{'id': 201, 'name': 'Jenny', 'class': 12, 'stream': 'Non-medical', 'marks': {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}, 'attendance': 75}
>>> student.keys()
dict_keys(['id', 'name', 'class', 'stream', 'marks', 'attendance'])
>>> keys = student.keys()
>>> len(keys)
6
>>> keys[0]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    keys[0]
TypeError: 'dict_keys' object is not subscriptable
>>> keys = list(student.keys())
>>> keys
['id', 'name', 'class', 'stream', 'marks', 'attendance']
>>> for x in student.keys():
	print(x)

	
id
name
class
stream
marks
attendance
>>> for x in list(student.keys()):
	print(x)

	
id
name
class
stream
marks
attendance
>>> for x in list(student.keys()):
	print(x, student[x])

	
id 201
name Jenny
class 12
stream Non-medical
marks {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}
attendance 75
>>> for key in list(student.keys()):
	print(key, student[key])

	
id 201
name Jenny
class 12
stream Non-medical
marks {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}
attendance 75
>>> for x in student.values():
	print(x)

	
201
Jenny
12
Non-medical
{'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}
75
>>> for x in student.items():
	print(x)

	
('id', 201)
('name', 'Jenny')
('class', 12)
('stream', 'Non-medical')
('marks', {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30})
('attendance', 75)
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> dict.fromkeys(keys)
{'id': None, 'name': None, 'class': None, 'stream': None, 'marks': None, 'attendance': None}
>>> dict.fromkeys(keys, 'NA')
{'id': 'NA', 'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'NA'}
>>> employee = dict.fromkeys(keys, 'NA')
>>> student = dict.fromkeys(keys, 'NA')
>>> student['id'] = 101
>>> student
{'id': 101, 'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'NA'}
>>> 
>>> student['id']
101
>>> student.get('id')
101
>>> student.pop()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    student.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> student.popitem()
('attendance', 'NA')
>>> student.popitem()
('marks', 'NA')
>>> student
{'id': 101, 'name': 'NA', 'class': 'NA', 'stream': 'NA'}
>>> student.pop('name')
'NA'
>>> student.pop('id')
101
>>> employee
{'id': 'NA', 'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'NA'}
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact" : [124, 3446, 467, 57668]
	}
>>> employee['department'] = 'finance'
>>> del employee['department']
>>> employee['department'] = 'HR'
>>> 
>>> employee['project'] = "Not assigned yet"
>>> employee['project'] = "Phoenix"
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'contact': [124, 3446, 467, 57668], 'department': 'HR', 'project': 'Phoenix'}
>>> employee['project'] = "Not assigned yet"
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'contact': [124, 3446, 467, 57668], 'department': 'HR', 'project': 'Not assigned yet'}
>>> employee['project'] = "Phoenix"
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'contact': [124, 3446, 467, 57668], 'department': 'HR', 'project': 'Phoenix'}
>>> employee.setdefault('project', 'Not assigned yet')
'Phoenix'
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'contact': [124, 3446, 467, 57668], 'department': 'HR', 'project': 'Phoenix'}
>>> del employee['project']
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'contact': [124, 3446, 467, 57668], 'department': 'HR'}
>>> employee.setdefault('project', 'Not assigned yet')
'Not assigned yet'
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'contact': [124, 3446, 467, 57668], 'department': 'HR', 'project': 'Not assigned yet'}
>>> employee.update(student)
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'contact': [124, 3446, 467, 57668], 'department': 'HR', 'project': 'Not assigned yet', 'class': 'NA', 'stream': 'NA'}
>>> student
{'class': 'NA', 'stream': 'NA'}
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact" : [124, 3446, 467, 57668]
	}
>>> student = {
	"id" : 201,
	"name" : "Jenny",
	"class" : 12,
	"stream" : "Non-medical",
	"marks" : {
		"english" : 95,
		"maths" : 64,
		"physics" : 70,
		"chemistry" : 80,
		"cs" : 90,
		"ped" : 30
		},
	"attendance" : 75
	}
>>> 
>>> employee.update(student)
>>> employee
{'id': 201, 'name': 'Jenny', 'salary': 15000, 'designation': 'Developer', 'department': 'IT', 'contact': [124, 3446, 467, 57668], 'class': 12, 'stream': 'Non-medical', 'marks': {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}, 'attendance': 75}
>>> employee['attendance']
75
>>> del employee['attendance']
>>> employee
{'id': 201, 'name': 'Jenny', 'salary': 15000, 'designation': 'Developer', 'department': 'IT', 'contact': [124, 3446, 467, 57668], 'class': 12, 'stream': 'Non-medical', 'marks': {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}}
>>> employee['attendance'] = student['attendance']
>>> employee
{'id': 201, 'name': 'Jenny', 'salary': 15000, 'designation': 'Developer', 'department': 'IT', 'contact': [124, 3446, 467, 57668], 'class': 12, 'stream': 'Non-medical', 'marks': {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}, 'attendance': 75}
>>> 
>>> employee.update( 75 )
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    employee.update( 75 )
TypeError: 'int' object is not iterable
>>> employee.update( student['attendance'] )
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    employee.update( student['attendance'] )
TypeError: 'int' object is not iterable
>>> employee.update( student['marks'] )
>>> 
>>> employee
{'id': 201, 'name': 'Jenny', 'salary': 15000, 'designation': 'Developer', 'department': 'IT', 'contact': [124, 3446, 467, 57668], 'class': 12, 'stream': 'Non-medical', 'marks': {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}, 'attendance': 75, 'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'ped': 30}
>>> 
>>> 
>>> set1 = {}
>>> type(set1)
<class 'dict'>
>>> set1 = set()
>>> set1
set()
>>> type(set1)
<class 'set'>
>>> 
>>> set1 = {10,20,30}
>>> set1
{10, 20, 30}
>>> set1 = {10,20,30,'forty',50.5,True,'sixty','python','hello','Jenny','Ram',False,1}
>>> set1
{False, True, 10, 'sixty', 'hello', 'Jenny', 50.5, 20, 'forty', 'Ram', 'python', 30}
>>> set1 = {10,20,30,'forty',50.5,True,'sixty','python','hello','Jenny','Ram',False,1,10,20,30}
>>> set1
{False, True, 10, 'sixty', 'hello', 'Jenny', 50.5, 20, 'forty', 'Ram', 'python', 30}
>>> # set can contain only unique elements
>>> set1 = {10,20,30,'forty',50.5,True,'sixty','python','hello','Jenny','Ram',False,1,10,20,30}
>>> set1
{False, True, 10, 'sixty', 'hello', 'Jenny', 50.5, 20, 'forty', 'Ram', 'python', 30}
>>> set1 = {10,20,30,'forty',50.5,True,'sixty','python','hello','Jenny','Ram','Anna','Shyam',False,1,10,20,30}
>>> set1
{False, True, 10, 'sixty', 'hello', 'Jenny', 50.5, 20, 'Anna', 'Shyam', 'forty', 'Ram', 'python', 30}
>>> set1 = {10,20,30,'forty',50.5,True,'sixty','python','hello','Jenny','Ram','Anna','Shyam','python is very easy to learn',False,1,10,20,30}
>>> set1
{False, True, 10, 'python is very easy to learn', 'sixty', 'hello', 'Jenny', 50.5, 20, 'Anna', 'Shyam', 'forty', 'Ram', 'python', 30}
>>> 
>>> #hashing algorithm
>>> # random positions in the set for each value -> there is no index or key and the values gte random positions so there is no direct way to access a particular element
>>> for value in set1:
	print(value)

	
False
True
10
python is very easy to learn
sixty
hello
Jenny
50.5
20
Anna
Shyam
forty
Ram
python
30
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set1.add("some text")
>>> set1
{False, True, 10, 'python is very easy to learn', 'sixty', 'hello', 'Jenny', 50.5, 'some text', 20, 'Anna', 'Shyam', 'forty', 'Ram', 'python', 30}
>>> set2 = {'sixty', 'hello', 'Jenny', 50.5, 'some text', 20, 'Anna', 'Shyam', 'forty', 'Ram', 'python', 30}
>>> set1 - set2
{False, True, 10, 'python is very easy to learn'}
>>> set2 - set1
set()
>>> set2 = {'sixty', 'hello', 'Jenny', 50.5, 'some text', 20, 'Anna', 'Shyam', 'forty', 'Ram', 'python', 30, 40, 50}
>>> set2 - set1
{40, 50}
>>> set2.difference(set1)
{40, 50}
>>> set2.difference_update(set1)   # set2 = set2 - set1
>>> set2
{50, 40}
>>> set2.discard(100)
>>> set2.remove(100)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    set2.remove(100)
KeyError: 100
>>> set2.discard(10)
>>> set2.remove(20)
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    set2.remove(20)
KeyError: 20
>>> set2 = {'sixty', 'hello', 'Jenny', 50.5, 'some text', 20, 'Anna', 'Shyam', 'forty', 'Ram', 'python', 30, 40, 50}
>>> set2.discard(10)
>>> set2
{40, 'hello', 'sixty', 'Jenny', 50.5, 50, 20, 'Anna', 'Shyam', 30, 'forty', 'Ram', 'python', 'some text'}
>>> set2.discard(20)
>>> set2
{40, 'hello', 'sixty', 'Jenny', 50.5, 50, 'Anna', 'Shyam', 30, 'forty', 'Ram', 'python', 'some text'}
>>> set2.remove(50)
>>> set1.intersection(set2)
{'sixty', 'hello', 'Jenny', 50.5, 'some text', 'Shyam', 'Anna', 'forty', 'Ram', 'python', 30}
>>> set1.union(set2)
{False, True, 10, 'python is very easy to learn', 'Jenny', 20, 'Shyam', 30, 40, 'sixty', 'hello', 50.5, 'Anna', 'forty', 'Ram', 'python', 'some text'}
>>> set1.isdisjoint(set2)
False
>>> set3 = {99,88,77}
>>> set1.isdisjoint(set3)
True
>>> set4 = {50.5, 'some text', 20}
>>> set2.issuperset(set4)
False
>>> set4 = {50.5, 'some text', 40}
>>> set2
{40, 'hello', 'sixty', 'Jenny', 50.5, 'Anna', 'Shyam', 30, 'forty', 'Ram', 'python', 'some text'}
>>> set2.issuperset(set4)
True
>>> set4.issubset(set2)
True
>>> set2.issuperset(set3)
False
>>> set2.pop()  # pop will delete elements from the front of set (it just starts looking for a value to pop it)
40
>>> 
>>> set2.pop()
'hello'
>>> 
>>> 
>>> set2.pop()
'sixty'
>>> set1 - set2
{False, True, 10, 'python is very easy to learn', 'sixty', 'hello', 20}
>>> set2 - set1
set()
>>> set2 = {'sixty', 'hello', 'Jenny', 50.5, 'some text', 20, 'Anna', 'Shyam', 'forty', 'Ram', 'python', 30, 40, 500}
>>> set2 - set1
{40, 500}
>>> set1.symmetric_difference(set2)
{False, True, 40, 10, 'python is very easy to learn', 500}
>>> set1 - set2
{False, True, 10, 'python is very easy to learn'}
>>> 
>>> (set1 - set2).union( set2 - set1 )
{False, True, 'python is very easy to learn', 500, 40, 10}
>>> f_set = frozenset( set1 )
>>> f_set
frozenset({False, True, 10, 'python is very easy to learn', 'Jenny', 20, 'Shyam', 30, 'sixty', 'hello', 50.5, 'Anna', 'forty', 'Ram', 'python', 'some text'})
>>> dir( f_set )
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> f_set.add(10)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    f_set.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
