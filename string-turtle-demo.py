Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello Everyone, this is PythOn prOgramming"
>>> str1 = 'Hello Everyone, this is PythOn prOgramming'
>>> str1 = 'a'
>>> type(str1)
<class 'str'>
>>> # string is a collection of one or more characters
>>> # char arr[] = ['h', 'e', 'l', 'l', 'o']
>>> str1[0]
'a'
>>> str1[1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str1[1]
IndexError: string index out of range
>>> str1 = 'Hello Everyone, this is PythOn prOgramming'
>>> str1[0]
'H'
>>> str1[1]
'e'
>>> str1[2]
'l'
>>> str1[3]
'l'
>>> str1[4]
'o'
>>> len(str1)
42
>>> str1[42]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str1[42]
IndexError: string index out of range
>>> str1[41]
'g'
>>> str1[40]
'n'
>>> str1[39]
'i'
>>> str1[-1]
'g'
>>> str1[-2]
'n'
>>> str1[-3]
'i'
>>> # a part of string - substring - string slicing
>>> str1
'Hello Everyone, this is PythOn prOgramming'
>>> str1[0]
'H'
>>> str1[0:10]
'Hello Ever'
>>> # str1[ starting index : stopping index ]
>>> str1[0:5]
'Hello'
>>> str1[20]
' '
>>> str1[21]
'i'
>>> str1[24]
'P'
>>> str1[24:30]
'PythOn'
>>> str1[31:41]
'prOgrammin'
>>> str1[31:42] # silently it just gives the data which it is able to find
'prOgramming'
>>> str1[31:420]
'prOgramming'
>>> str1[100:420]
''
>>> str1 = 'Hello Everyone, this is PythOn prOgramming.mp3'
>>> str1[-1:-5]
''
>>> str1[-4:-1]
'.mp'
>>> str1[-4:0]
''
>>> str1[-1 : -5 : 1]
''
>>> str1[-1 : -5 : -1]
'3pm.'
>>> str1[ -4 : -1 : 1]
'.mp'
>>> str1[ -4 ]
'.'
>>> str1[ -4 : ]
'.mp3'
>>> str1[10:]
'yone, this is PythOn prOgramming.mp3'
>>> str1[ : ]
'Hello Everyone, this is PythOn prOgramming.mp3'
>>> str1[ : : -1 ]
'3pm.gnimmargOrp nOhtyP si siht ,enoyrevE olleH'
>>> # string reverse using slicing
>>> # str1[ starting index : stopping index : jump ]
>>> str1[10 : 40 : 1]
'yone, this is PythOn prOgrammi'
>>> str1[10 : 40 : 2]
'yn,ti sPtO rgam'
>>> str1[10 : 40 : 5]
'y  y r'
>>> str1[10 : 5 : -1]
'yrevE'
>>> str1 = 'hello python'
>>> str1 = "hello python"
>>> str1 = 'what's up'
SyntaxError: invalid syntax
>>> str1 = "what's up"
>>> str1
"what's up"
>>> print(str1)
what's up
>>> str1 = 'Dwayne "Rock" Johnson'
>>> print(str1)
Dwayne "Rock" Johnson
>>> str1 = 'what's going on with Dwayne "Rock" Johnson'
SyntaxError: invalid syntax
>>> str1 = "what's going on with Dwayne "Rock" Johnson"
SyntaxError: invalid syntax
>>> str1 = "what's going on with Dwayne \"Rock\" Johnson"  #   \ -> escape character
>>> print(str1)
what's going on with Dwayne "Rock" Johnson
>>> str1 = 'what\'s going on with Dwayne "Rock" Johnson'  #   \ -> escape character
>>> print(str1)
what's going on with Dwayne "Rock" Johnson
>>> str1 = 'hello jenny.what\'s going on with Dwayne "Rock" Johnson'  #   \ -> escape character
>>> print(str1)
hello jenny.what's going on with Dwayne "Rock" Johnson
>>> str1 = 'hello jenny.\nwhat\'s going on with Dwayne "Rock" Johnson'  #   \n -> provide a new line
>>> print(str1)
hello jenny.
what's going on with Dwayne "Rock" Johnson
>>> 
>>> dir( str )
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> sizeof
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    sizeof
NameError: name 'sizeof' is not defined
>>> size
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    size
NameError: name 'size' is not defined
>>> str1.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> print( str1.__doc__ )
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
>>> print( int.__doc__ )
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1
'hello jenny.\nwhat\'s going on with Dwayne "Rock" Johnson'
>>> str1 = 'hello jenny.whats going on with Dwayne Rock Johnson'
>>> str1.capitalize()
'Hello jenny.whats going on with dwayne rock johnson'
>>> # Dwayne Rock Johnson      Google Chrome      IDE -> Integrated Development Environment
>>> str1.title()
'Hello Jenny.Whats Going On With Dwayne Rock Johnson'
>>> str1.center(100)
'                        hello jenny.whats going on with Dwayne Rock Johnson                         '
>>> str1.center(100, '$')
'$$$$$$$$$$$$$$$$$$$$$$$$hello jenny.whats going on with Dwayne Rock Johnson$$$$$$$$$$$$$$$$$$$$$$$$$'
>>> str1.center(200, '$')
'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$hello jenny.whats going on with Dwayne Rock Johnson$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
>>> str1.center(80, '$')
'$$$$$$$$$$$$$$hello jenny.whats going on with Dwayne Rock Johnson$$$$$$$$$$$$$$$'
>>> str1.center(10, '$')
'hello jenny.whats going on with Dwayne Rock Johnson'
>>> str1.center(50, '$')
'hello jenny.whats going on with Dwayne Rock Johnson'
>>> str1.center(60, '$')
'$$$$hello jenny.whats going on with Dwayne Rock Johnson$$$$$'
>>> str1.count( 'o' )
6
>>> str1.count( 'on' )
2
>>> str1.count( 'hello' )
1
>>> str1.find( 'o' )
4
>>> str1[4]
'o'
>>> str1.find( 'o', 5 )
19
>>> str1.find( 'o', 20 )
24
>>> str1.find( 'o', 25 )
40
>>> str1.find( 'o', 41 )
45
>>> str1.find( 'o', 46 )
49
>>> str1.find( 'o', 50 )
-1
>>> str1[50]
'n'
>>> len(str1)
51
>>> str1.index( 'o', 50 )
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    str1.index( 'o', 50 )
ValueError: substring not found
>>> str1.index( 'o', 40 )
40
>>> str1.index( 'o', 30 )
40
>>> str1.index( 'o', 20 )
24
>>> str1.endswith('on')
True
>>> str1.endswith('Johnson')
True
>>> str1.endswith('johnson')
False
>>> str1.startswith('hello')
True
>>> str1.startswith('hello python')
False
>>> str2 = 'abhja788abna'
>>> str2.isalpha()
False
>>> str2.isalnum()
True
>>> str1.isalpha()
False
>>> str1
'hello jenny.whats going on with Dwayne Rock Johnson'
>>> str2 = 'hellojenny'
>>> str1.isalpha()
False
>>> str2.isalpha()
True
>>> str1 = 'snskn bsjb lsk2345'
>>> str1.isalnum()
False
>>> str1 = 'snskn$bsjbπlsk2345'
>>> str1.isalnum()
False
>>> str1.isdecimal()
False
>>> str2 = "348940384905"
>>> str1.isdecimal()
False
>>> str2.isdecimal()
True
>>> str1 = 'snskn$bsjbπlsk2345'
>>> str1.isascii()
False
>>> ord('π')
960
>>> str1 = 'snskn$bsjb~lsk2345'
>>> str1.isascii()
True
>>> str1.islower()
True
>>> str1 = 'snskn$bsjb~Lsk2345'
>>> str1.islower()
False
>>> 'π'.isprintable()
True
>>> '\n'.isprintable()
False
>>> str2 = 'abc\ndef'
>>> print(str2)
abc
def
>>> str1.center(50)
'                snskn$bsjb~Lsk2345                '
>>> str1.center(50, '$')
'$$$$$$$$$$$$$$$$snskn$bsjb~Lsk2345$$$$$$$$$$$$$$$$'
>>> str1.ljust(50, '$')
'snskn$bsjb~Lsk2345$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
>>> str1.rjust(50, '$')
'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$snskn$bsjb~Lsk2345'
>>> # immutable
>>> # int, float, bool, str -> immutable objects -> cannot be changed
>>> a = 10
>>> a + 1
11
>>> a = 10
>>> id(a)
4414807504
>>> a = a+1
>>> a
11
>>> id(a)
4414807536
>>> str2 = "svrbb"
>>> str2[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    str2[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> str1
'snskn$bsjb~Lsk2345'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> str1
'snskn$bsjb~Lsk2345'
>>> str1 = 'hello jenny.whats going on with Dwayne Rock Johnson'
>>> str1.split()
['hello', 'jenny.whats', 'going', 'on', 'with', 'Dwayne', 'Rock', 'Johnson']
>>> str1 = 'hello jenny.whats going on with Dwayne Rock Johnson'
>>> str1 = 'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1.split()
['hello', 'jenny.', 'whats', 'going', 'on', 'with', 'Dwayne', 'Rock', 'Johnson']
>>> words = str1.split()
>>> ' '.join(words)
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> '_'.join(words)
'hello_jenny._whats_going_on_with_Dwayne_Rock_Johnson'
>>> '*'.join(words)
'hello*jenny.*whats*going*on*with*Dwayne*Rock*Johnson'
>>> '*****'.join(words)
'hello*****jenny.*****whats*****going*****on*****with*****Dwayne*****Rock*****Johnson'
>>> ' '.join(words)   #  join the words together present in array using ' ' character
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> 
>>> 
>>> str1.split()
['hello', 'jenny.', 'whats', 'going', 'on', 'with', 'Dwayne', 'Rock', 'Johnson']
>>> str1.split(' ', 1)
['hello', 'jenny. whats going on with Dwayne Rock Johnson']
>>> str1.split(' ', 2)
['hello', 'jenny.', 'whats going on with Dwayne Rock Johnson']
>>> str1.split(' ', 20)
['hello', 'jenny.', 'whats', 'going', 'on', 'with', 'Dwayne', 'Rock', 'Johnson']
>>> str1.split('.', 20)
['hello jenny', ' whats going on with Dwayne Rock Johnson']
>>> 
>>> 
>>> str1 = "                  Python Developer                                   "
>>> print(str1)
                  Python Developer                                   
>>> print( str1.strip() )  # remove leading and trailing spaces
Python Developer
>>> print("*" + str1 + "*")
*                  Python Developer                                   *
>>> print("*" + str1.strip() + "*")
*Python Developer*
>>> 
>>> str1.replace( 'o', 'x' )
'                  Pythxn Develxper                                   '
>>> str1 = 'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1.replace( 'o', 'x' )
'hellx jenny. whats gxing xn with Dwayne Rxck Jxhnsxn'
>>> str1
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> id(str1)
4468040768
>>> str1
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1 = str1.replace('o', 'x')
>>> str1
'hellx jenny. whats gxing xn with Dwayne Rxck Jxhnsxn'
>>> id(str1)
4468041184
>>> 
>>> import turtle
>>> screen = turtle.Screen()
>>> screen.bgcolor('black')
>>> pen = turtle.Pen()
>>> pen.color('white')
>>> pen.turtlesize(3)
>>> pen.shape('turtle')
>>> pen.forward(100)
>>> pen.reset()
>>> pen.color('white')
>>> pen.turtlesize(3)
>>> pen.width(3)
>>> pen.forward(100)
>>> pen.left(90)
>>> pen.forward(100)
>>> pen.left(90)
>>> pen.forward(100)
>>> pen.left(90)
>>> pen.forward(100)
>>> pen.left(90)
>>> pen.forward(200)
>>> pen.left(90)
>>> pen.forward(300)
>>> pen.left(90)
>>> pen.forward(200)
>>> pen.left(90)
>>> pen.forward(300)
>>> pen.left(90)
>>> 
