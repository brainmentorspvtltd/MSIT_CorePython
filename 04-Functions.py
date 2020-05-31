x = 100


def outer():
    # x = 200  # local variable
    global x
    x = x + 1
    print("Outer fn called...", x)

    def inner():
        print("inner fn called")

    # inner()

    print("Outer fn going to finish...")

    return inner


returnedFn = outer()
returnedFn()
# inner()
