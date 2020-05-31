def checkEven(num):
    return num % 2 == 0  # it will return either true or false


numbers = list(range(1, 101))

result_list = list(filter(lambda num: num % 2 == 0, numbers))
print(result_list)

# print(checkEven(num))

list1 = []

for num in numbers:
    result = checkEven(num)
    list1.append(result)

print(list1)

# map fn calls the specified fn for each value in our list and store the returned result in some other list
# filter fn calls the specified fn for each value in our list but doesn't store the returned value (true or false), instead it checks for the returned value - if returned value is true then the argument that was sent to the function (2,4,6,8 ) is stored in a new list
