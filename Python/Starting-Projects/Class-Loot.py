import random

class Main_Loot(object):
    def __init__(self):
        self.apple = 200
        self.oranges = 200
        self.watermelons = 200
        self.bananas = 200

Loot = Main_Loot()

Store = {
        "Apple": Loot.apple,
        "Oranges": Loot.oranges,
        "Watermelons": Loot.watermelons,
        "Bananas": Loot.bananas
        }
for K in Store:
        print K ,": " + str(Store[K])


Apple_demand = random.randint(10, 20)

print ("\n\n\tApples")

while Loot.apple > 30:
    Loot.apple -= Apple_demand
    print Loot.apple

    if Loot.apple <= 30:
        print "Out of Stock"


Oranges_demand = random.randint(10, 30)

print "\n\n\t Oranges "

while Loot.oranges > 30:
    Loot.oranges -= Oranges_demand
    print Loot.oranges

    if Loot.oranges <= 30:
        print ("Out of stock")

print ("\n\n\t Watermelons")

Watermelons_demand = random.randint(20, 40)

while Loot.watermelons > 30:
    Loot.watermelons -= Watermelons_demand
    print Loot.watermelons

    if Loot.watermelons <= 30:
        print ("Out of Stock")
        break

print ("\n\n\t Bananas")

Bananas_demand = random.randint(40, 50)

while Loot.bananas > 30:
    Loot.bananas -= Bananas_demand
    print Loot.bananas

    if Loot.bananas <= 30:
        print ("Out of stock")
