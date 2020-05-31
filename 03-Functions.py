def inputNumbers():
    a = input("Enter first number: ")  # local variable
    b = input("Enter second number: ")
    return a, b


def calc(operator):
    x, y = inputNumbers()
    # eval("10 / 10")
    print(eval(x + operator + y))
    # eval uses postfix expression evaluation


print('''
    1. Add
    2. Sub
    3. Mul
    4. Div
''')

choice = int(input("Enter your choice: "))

operations = {
    1: '+',   # pass only the fn reference, dont use () otherwise fn will get called automatically
    2: '-',
    3: '*',
    4: '/'
}

calc(operations.get(choice))
