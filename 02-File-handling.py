import csv

fileStream = open("users.csv", "a")

print('''
    1. Login
    2. Register
''')

choice = int(input("Enter choice: "))
emailExists = False

if choice == 2:
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    with open("users.csv", "a") as fileStream:
        reader = csv.reader(fileStream)
        for row in reader:
            # print(row)
            emailFromDB = row[1]
            if email == emailFromDB:
                print("Email already exists.. Try to login please..")
                emailExists = True
                break

    if not emailExists:
        with open("users.csv", "a", newline='') as fileStream:
            writer = csv.writer(fileStream)
            writer.writerow([name, email, password])
        print("Registration successful...")


# csv -> comma separated values

# ram kumar,ram@gmail.com,ram1234


print("Program ends here")
