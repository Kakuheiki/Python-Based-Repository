the_count = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Pears", "Apricots"]
change = [1, "Pennies", 2, "Dimes",3, "Quarters"]

for number in the_count:
    print ("This is the count: %s") % (number)

for fruit in fruits:
    print ("A fruit of type: %s") % (fruit)

for i in change:
    print ("I got %r") % (i)

elements = []

for i in range(0,6):
    print ("Adding %d to the list.") % (i)
    elements.append(i)

for i in elements:
    print ("elements was: %d") % i    
