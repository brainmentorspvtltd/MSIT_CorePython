def temp_convert(c):
    return 9 / 5 * c + 32
    # print()   #unreachable code

# a function that has a return statement in its first line can be converted to a lambda expression
# syntax for lambda ->   lambda param1, param2, param3 : return statement
# lambda expression - anonymous fns - single line fns


temp = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# f = temp_convert(temp)
# print(f)

# fah_list = list(map(temp_convert, temp))

fah_list = list(map(lambda c: 9 / 5 * c + 32, temp))

print(fah_list)

f_list = []

for t in temp:
    f = temp_convert(t)
    f_list.append(f)

print(f_list)

'''
list1 = [1,2,3,4,5]
>>> list2 = list1
>>> list2 is list1
True
>>> list3 = list1.copy()
>>> list3 is list1
False
>>> list3 is not list1
True

>>> def add(num1, num2):
...     return num1 + num2
... 
>>> lambda num1,num2 : num1 + num2
<function <lambda> at 0x107b4b8c8>
>>> '''
