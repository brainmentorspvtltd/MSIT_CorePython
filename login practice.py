import csv

fileStream = open("users.csv", "a")

print('''
    1. Login
    2. Register
    ''')
choice = int(input("Enter choices: "))

if choice == 1:
    # isLoginSuccessful = False    # flag variable
    email = input("Enter Emails: ")
    password = input("Enter Password: ")

    with open("users.csv") as fileStream:
        reader = csv.reader(fileStream)
        for row in reader:
            emailFromDB = row[1]
            passwordFromDB = row[2]
            if email == emailFromDB and password == passwordFromDB:
                print("Login Successful")
                # isLoginSuccessful = True
                break

        # if not isLoginSuccessful:
        #     print("Login Failure....pls try to Register")

        else:
            print("Login Failure....pls try to Register")
# for-else block
# else says i'm a post-script block of for loop
# else says if 'for loop' runs completely till the end then I will also run
# else says if 'for loop' is broken in between then I will not run

if choice == 2:

    emailExists = False
    name = input("Enter Name: ")
    email = input("Enter Emails: ")
    password = input("Ente Password: ")

    with open("users.csv") as fileStream:
        reader = csv.reader(fileStream)
        for row in reader:
            # print row
            emailFromDB = row[1]
            if email == emailFromDB:
                print("Email already exists... Try to login please")
                emailExists = True
                break

    if not emailExists:
        with open("users.csv", "a", newline='') as fileStream:
            writer = csv.writer(fileStream)
            writer.writerow([name, email, password])
        print()
        print("Registration successful")
        print()


# csv -> commaseparatedvalues
