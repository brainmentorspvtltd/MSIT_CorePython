x = 19   # global variables (accessible to anyone in the file)
y = 10

# def fn_name( param1, param2, param3, param4, param5, param6):
# statement1
# statememt2
# return statement


def inputNumbers():
    a = int(input("Enter first number: "))  # local variable
    b = int(input("Enter second number: "))
    return a, b   # always a single value is returned


# def add(x, y):
#     # x, y = inputNumbers()
#     print(x + y)

# rule -> positional arguments should always come before the default arguments
# in parameter list, *args should always be the last argument
# otherwise it will consume all the values coming in and the other variables will starve
def add(x=0, y=1, *z):  # default arguments,  *args (varargs) -> variable args
    print(x + y)
    print("Z is", z)

# Overriding - if you create two fns with a same name then the fn written at the last will be the active fn and the upper one will become deactive


def add(*z):
    sum = 0
    for value in z:
        sum += value
    print("Sum is ", sum)


add()
add(10)
add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)


def calc():
    return x + y, x - y, x * y, x / y, x % y, x ** y  # packing


# result = calc()
# print("Result is ", result)
# a = result[0]
# b = result[1]
# c = result[2]
# d = result[3]

# When we use *args in unpacking, then it works sensibly
# Even if *args is placed at the starting of the list then also it will allow other variables to have some values and not consume everything itself
*e, a, b, c, d = calc()  # unpacking
# e = calc()   # no unpacking of *args required
print("A is", a)
print("B is", b)
print("C is", c)
print("D is", d)
print("E is", e)


def sub(x, y):
    # x, y = inputNumbers()
    print(x - y)


def mul(x, y):
    # x, y = inputNumbers()
    print(x * y)


def div(x, y):
    # x, y = inputNumbers()
    print(x / y)


add()
add(10, 20)
sub(20, 10)
mul(123, 56)
div(12345, 567)


def printEmployeeDetails(id, name, salary='Not known', designation='To be decided', department='To be provided later', city='Address not known', **otherDetails):
    print("Id is", id)
    print("Name is", name)
    print("Salary is", salary)
    print("Designation is", designation)
    print("Department is", department)
    print("City is", city)
    print("Other details ", otherDetails)


# keyword based passing of arguments
printEmployeeDetails(id=101, city="Delhi", name="Ram")
printEmployeeDetails(id=101, city="Delhi", name="Ram",
                     leavesTaken=10, ticketsDone=20, age=30)
# we can use positional arguments
# we dont want to send all the arguments then we can use keyword arguments
# if we want to supply extra data then it should also be keyword argument
# because after keyword args, positional args are not allowed
# but to supply extra if we use keywords then fn gives error that it desnt have the key to which you want to provide data even if fn contains *args
# so we need to use **args to consume all the extra keyword args
