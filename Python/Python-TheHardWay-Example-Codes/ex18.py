def print_two_again(arg1, arg2):
    return ("Arg1: %r, Arg2: %r") % (arg1, arg2)

def print_one(arg1):
    return ("arg1: %r") % (arg1)

def print_none():
    return ("I got nothin.")

Choice = raw_input("1, 2 or 3:  ")

if Choice == "1":
    arg1 = raw_input("First Arg: ")
    arg2 = raw_input("Second Arg: ")
    print print_two_again(arg1, arg2)

if Choice == "2":
    arg1 = raw_input("Arg1: ")
    print print_one(arg1)

if Choice == "3":
    arg = "a"
    print print_none()
