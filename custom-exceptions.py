correctPIN = 1234
balance = 10000


def checkPin():
    PIN = int(input("Enter PIN number: "))
    if PIN != correctPIN:
        raise ValueError("Incorrect PIN")
    print("PIN correct")
    return True


def checkBalance():
    amount = int(input("Enter amount to withdraw: "))
    if amount > balance:
        raise ValueError("Insufficient balance")
    return amount


def withdraw():
    global balance
    isPINCorrect = checkPin()
    if isPINCorrect:
        amount = checkBalance()
        balance -= amount
        print("Withdrawal successful..", balance, "left")


try:
    withdraw()
except ValueError as ex:
    print("Value Error", ex)
except Exception as ex:
    print("Some exception occured..", ex)
else:
    print("Thank you for visiting us!!")
