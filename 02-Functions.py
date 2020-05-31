def inputNumbers():
    a = int(input("Enter first number: "))  # local variable
    b = int(input("Enter second number: "))
    return a, b


def add():
    x, y = inputNumbers()
    print(x + y)


def sub():
    x, y = inputNumbers()
    print(x - y)


def mul():
    x, y = inputNumbers()
    print(x * y)


def div():
    x, y = inputNumbers()
    print(x / y)


def errorHandler():
    print("Wrong choice...")


print('''
    1. Add
    2. Sub
    3. Mul
    4. Div
''')

choice = int(input("Enter your choice: "))

operations = {
    1: add,   # pass only the fn reference, dont use () otherwise fn will get called automatically
    2: sub,
    3: mul,
    4: div
}

# operations[choice]()
operations.get(choice, errorHandler)()

# if choice == 1:
#     add()
# elif choice == 2:
#     sub()

'''
def first():
...     print("First called...")
...     return 1
... 
>>> def second():
...     print("Second called...")
...     return 2
... 
>>> operations = {
...     1: first(),
...     2: second()
... }
First called...
Second called...
>>> operations
{1: 1, 2: 2}
operations = {
...     1: first,
...     2: second
... }
>>> 
>>> 
>>> print
<built-in function print>
>>> first
<function first at 0x1091268c8>
>>> second
'''
