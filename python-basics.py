Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 2
3
>>> print
<built-in function print>
>>> print("My name is Ram")
My name is Ram
>>> print("Hello, world")
Hello, world
>>> a = 10
>>> b = 20
>>> print("Sum of a and b is c")
Sum of a and b is c
>>> print("Sum of a and b is a+b")
Sum of a and b is a+b
>>> print("Sum of {} and {} is {}".format(a, b, a+b) )
Sum of 10 and 20 is 30
>>> print("Sum of {1} and {2} is {3}, Diff of {1} and {2} is {4}, Product of {1} and {2} is {5}, Quotient of {1} and {2} is {6}".format(a, b, a+b, a-b, a*b, a/b) )
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("Sum of {1} and {2} is {3}, Diff of {1} and {2} is {4}, Product of {1} and {2} is {5}, Quotient of {1} and {2} is {6}".format(a, b, a+b, a-b, a*b, a/b) )
IndexError: tuple index out of range
>>> print("Sum of {0} and {1} is {2}, Diff of {0} and {1} is {3}, Product of {0} and {1} is {4}, Quotient of {0} and {1} is {5}".format(a, b, a+b, a-b, a*b, a/b) )
Sum of 10 and 20 is 30, Diff of 10 and 20 is -10, Product of 10 and 20 is 200, Quotient of 10 and 20 is 0.5
>>> print("Sum of {a} and {b} is {a+b}, Diff of {a} and {b} is {a-b}, Product of {a} and {b} is {a*b}, Quotient of {a} and {b} is {a/b}")
Sum of {a} and {b} is {a+b}, Diff of {a} and {b} is {a-b}, Product of {a} and {b} is {a*b}, Quotient of {a} and {b} is {a/b}
>>> print( f"Sum of {a} and {b} is {a+b}, Diff of {a} and {b} is {a-b}, Product of {a} and {b} is {a*b}, Quotient of {a} and {b} is {a/b}")
Sum of 10 and 20 is 30, Diff of 10 and 20 is -10, Product of 10 and 20 is 200, Quotient of 10 and 20 is 0.5
>>> 
>>> name = input("Enter your name: ")
Enter your name: Ram
>>> print(f"Welcome {name}")
Welcome Ram
>>> name = input("Enter your name: ")
Enter your name: Jenny
>>> print(f"Welcome {name}")
Welcome Jenny
>>> 
>>> f_num = input("Enter first number: ")
Enter first number: 99
>>> s_num = input("Enter second number: ")
Enter second number: 88
>>> first = input("Enter first number: ")
Enter first number: 99
>>> s_num = input("Enter second number: ")
Enter second number: 
>>> second = input("Enter second number: ")
Enter second number: 88
>>> print(first+second)
9988
>>> # input fn always return some text value (string) -> concatenation
>>> 
>>> first = int( input("Enter first number: ") )
Enter first number: 99
>>> type( first )
<class 'int'>
>>> second = input("Enter second number: ")
Enter second number: 
88
>>> type(second)
<class 'str'>
>>> second = int( input("Enter second number: ") )
Enter second number: 88
>>> type(second)
<class 'int'>
>>> print( first + second )
187
>>> print("Sum of {0} and {1} is {2}, Diff of {0} and {1} is {3}, Product of {0} and {1} is {4}, Quotient of {0} and {1} is {5}".format(first, second, first + second, first - second, first * second, first / second) )
Sum of 99 and 88 is 187, Diff of 99 and 88 is 11, Product of 99 and 88 is 8712, Quotient of 99 and 88 is 1.125
>>> 
>>> 
>>> # binary number system - 0 and 1
>>> # octal number system - 0 to 7
>>> # decimal number system ( default ) - 0 to 9
>>> # hexadeciaml number system - 0 to 15, A - 10, B - 11, C - 12, D - 13, E - 14, F - 15
>>> 
>>> a = 99
>>> bin( a )
'0b1100011'
>>> # 0b tells us / Python that the number written after it is in binary system, not in decimal system
>>> b = 100011
>>> type(b)
<class 'int'>
>>> b = 0b100011
>>> type(b)
<class 'int'>
>>> int( b )
35
>>> b = 100011
>>> int( b )
100011
>>> int( 0b1100011 )
99
>>> oct( a )
'0o143'
>>> hex( a )
'0x63'
>>> int( 0o143 )
99
>>> int( 0x63 )
99
>>> int( 0x63A )
1594
>>> int( 0x63a )
1594
>>> 
>>> 1 + 22
23
>>> 1 - 2
-1
>>> 1 * 2
2
>>> 1 / 2
0.5
>>> 1 % 2
1
>>> 99 % 3
0
>>> 100 % 3
1
>>> 101 % 3
2
>>> 102 % 3
0
>>> 53635/433
123.86836027713626
>>> round( 53635/433 )
124
>>> type(123.86836027713626)
<class 'float'>
>>> int(123.86836027713626)
123
>>> 53635 // 433
123
>>> # floor division
>>> #  / -> classic division
>>> 
>>> pow( 2, 10 )
1024
>>> pow( 20, 10 )
10240000000000
>>> pow( 35353, 4 )
1562086549854182881
>>> 
>>> 35353 * 4
141412
>>> 35353 ** 4
1562086549854182881
>>> #   // is same as int()
>>> #   ** is same as pow()
>>> 
>>> # int, float, string, boolean, byte, complex
>>> a = 10
>>> type(int)
<class 'type'>
>>> type(a)
<class 'int'>
>>> a = 10.5 #dynamic typing
>>> type(a)
<class 'float'>
>>> a = "ten"
>>> type(a)
<class 'str'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = False
>>> type(a)
<class 'bool'>
>>> 
>>> # ascii table and unicode table
>>> # C,C++ character - (a,A,1,0,@, ,',) - 1 byte of memory
>>> # Python character -  2 bytes of memory
>>> a = "text"
>>> a = "टेक्स्ट"
>>> print(a)
टेक्स्ट
>>> a = "My name is πø¬˚∆˙©¥•µ©ç†§®∑ßç राम"
>>> print(a)
My name is πø¬˚∆˙©¥•µ©ç†§®∑ßç राम
>>> print("I have ₹10")
I have ₹10
>>> msg = "I have ₹10
SyntaxError: EOL while scanning string literal
>>> msg = "I have ₹10"
>>> msg.encode()
b'I have \xe2\x82\xb910'
>>> "I have \xe2\x82\xb910".decode()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    "I have \xe2\x82\xb910".decode()
AttributeError: 'str' object has no attribute 'decode'
>>> type("I have \xe2\x82\xb910")
<class 'str'>
>>> type( b"I have \xe2\x82\xb910")
<class 'bytes'>
>>> b"I have \xe2\x82\xb910".decode()
'I have ₹10'
>>> b"\xe2\x82\xb9".decode()
'₹'
>>> b"\xe3\x82\xb9".decode()
'ス'
>>> b"\xe3\x85\xb9".decode()
'ㅹ'
>>> b"\xe3\x85\xba".decode()
'ㅺ'
>>> 
>>> # 'a' -> 97
>>> # 'A' -> 65
>>> ord() # ordinal (ascii/unicode value)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    ord() # ordinal (ascii/unicode value)
TypeError: ord() takes exactly one argument (0 given)
>>> 
>>> 
>>> ord('a')
97
>>> ord('A')
65
>>> ord('₹')
8377
>>> chr(1000)
'Ϩ'
>>> chr(10000)
'✐'
>>> chr(99)
'c'
>>> chr(12345)
'〹'
>>> 
>>> 
>>> a
'My name is πø¬˚∆˙©¥•µ©ç†§®∑ßç राम'
>>> id(a)
4382411632
>>> id(b)
4411793040
>>> id(first)
4358531312
>>> id(second)
4358530960
>>> # hashcode -> code generation by hashing algorithm when the memory location was getting stored
>>> 
>>> type(a)
<class 'str'>
>>> # int a = 10
>>> # a.pow(2)
>>> # Everything in python is object
>>> a = 10
>>> a = 10.5
>>> a = "text"
>>> #a = &99
>>> #a = &88
>>> #a = &77
>>> 
>>> dir( int )
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a = 10
>>> a.__pow__(4)
10000
>>> "abc{}".format(a)
'abc10'
>>> # 4 + i5
>>> complex( 3, 6 )
(3+6j)
>>> complex_number = complex( 3, 6 )
>>> complex_number.real
3.0
>>> complex_number.imag
6.0
>>> int = 10
>>> type(str)
<class 'type'>
>>> type(bool)
<class 'type'>
>>> type(int)
<class 'int'>
>>> int()
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    int()
TypeError: 'int' object is not callable
>>> str()
''
>>> str = 10
>>> str()
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    str()
TypeError: 'int' object is not callable
>>> 
>>> str()
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    str()
TypeError: 'int' object is not callable
>>> 
>>> print("Sum is" + a)
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    print("Sum is" + a)
TypeError: can only concatenate str (not "int") to str
>>> print("Sum is" + str(a))
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    print("Sum is" + str(a))
TypeError: 'int' object is not callable
>>> 
