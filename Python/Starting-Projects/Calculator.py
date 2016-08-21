def add():
    print ("Sum")
    A = int(raw_input("Enter First number: "))
    B = int(raw_input("Enter Second number: "))
    return A + B

def rest():
    print ("Rest")
    A = int(raw_input("Enter First number: "))
    B = int(raw_input("Enter Second number: "))
    return A - B

def division():
    print ("Division")
    A = float(raw_input("Enter First number: "))
    B = float(raw_input("Enter Second number: "))
    return A / B

def multiplication():
    print ("Multiplication")
    A = int(raw_input("Enter First number: "))
    B = int(raw_input("Enter Second number: "))
    return A * B


print ("1: Addtion")
print ("2: Rest")
print ("3: Division")
print ("4: Multiplication")
print ("0: Quit")

while True:

    Choice = int(raw_input("What are you going to do?: "))

    if Choice == 1:
        print add()

    elif Choice == 2:
        print rest()

    elif Choice == 3:
        print division()

    elif Choice == 4:

        print multiplication()

    elif Choice == 0:
        exit()

    else:
        print "The value Enter value from 1-4"
