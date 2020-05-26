'''
*
**
***
****
*****
'''

for i in range(5):
    print('*' * (i + 1))  # string replication

print("------------------------")

'''for i in range(5):
    for j in range(5):
        print(i, j)'''

'''
*****
****
***
**
*
'''

'''
    *
   **
  ***
 ****
*****
'''

for i in range(5):
    print((" " * (4 - i)) + ("*" * (i + 1)))
    # print("$" * (4 - i), "*" * (i + 1), sep='')
    # print("Sum of",a,'and',b,'is',c)

print("------------------------")


'''
*****
 ****
  ***
   **
    *
'''

'''
    *
   ***
  *****
 *******
*********
'''

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

for i in range(9):
    if i <= 4:
        for j in range(4-i):
            print(" ", end='')
        for k in range(2*i+1):
            print("*", end='')
    else:
        for j in range(i - 4):
            print(" ", end='')
        # for k in range((2*i) - ((i-4)*4) + 1):
        for k in range((9-i)*2 - 1):
            print('*', end='')
    print()

print("------------------------")

for i in range(5):
    for j in range(4-i):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print()
for i in range(4):
    for j in range(i + 1):
        print(" ", end='')
    for k in range(7 - i * 2):
        print("*", end='')
    print()
