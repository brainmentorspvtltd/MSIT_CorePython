import io

# try block means try to run this code, if it contains any exception then hand over that exception to except block
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Division result is", num1 / num2)

    # list1 = [0, 1, 2, 3, 4]
    # print(list1[100])

    tuple1 = (0, 1, 2)
    del tuple1[0]

    with open("FileHandling.txt") as fileStream:
        fileStream.write("hello")

except ZeroDivisionError:
    print("Second number cannot be zero while perforimg division")
except IndexError:
    print("Index provided is not available in the list")
except io.UnsupportedOperation:
    print("Cannot write when file is opened in read mode")
except ValueError:
    print("Please enter valid integers")
except Exception as ex:
    print("Some exception occurred...", ex)

print("Program ends here")
