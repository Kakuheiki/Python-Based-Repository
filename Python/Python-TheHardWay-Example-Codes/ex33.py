def Time():
    a = int(raw_input("> "))
    i = 1
    numbers = []
    times = a


    while i < times:
        print ("At the top i is %d") % (i)
        numbers.append(i)
        i = i + 1
        print ("Numbers now: ", numbers)


print ("Hello")
print Time()
