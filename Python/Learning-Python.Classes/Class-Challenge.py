print "\t\tHeroes"
print "\n"

class BaseHero(object):
    def __init__(self, name, gender, age, Weapon):
        self.name = name
        self.gender = gender
        self.age = age
        self.weapon = Weapon
        self.health = 100
        self.damage = 50
        self.magic = 10

    def StrongTest(self):
        if (self.damage >= self.magic):
            return ("You are so STRONG!")
        else:
            return ("You are so Wise!")

    def printName(self):
        print self.name

class GreenLantern(BaseHero):
    def __init__(self, name, gender, age, Weapon):
        BaseHero.__init__(self, name, gender, age, Weapon)
        self.magic = 50
        self.damage = 10



class SwordsMan(BaseHero):
    def __init__(self, name, gender, age, Weapon):
        super(SwordsMan, self).__init__(name, gender, age, Weapon)
        self.damage = 60

class Archer(BaseHero):
    def __init__(self, name, gender, age, Weapon):
        super(Archer, self).__init__(name, age, gender, Weapon)
        self.damage = 40
        self.magic = 30


greenLantern = GreenLantern("Melisa", "Female", 16, "Staff")
swordsMan = SwordsMan("Gilbert", "Male", 15, "Ni-Toriu")
archer = Archer("Julia", "Female", 14, "Arc")

print "GreenLantern Weapon: " + greenLantern.weapon
print "SwordsMan Weapon: " + swordsMan.weapon
print "Archer Weapon: " + archer.weapon

print "\n"

print "GreenLantern Magic: " + str(greenLantern.magic)
print "SwordsMan Magic: " + str(swordsMan.magic)
print "Archer Magic: " + str(archer.magic)

print "\n"

print "GreenLantern Damage: " + str(greenLantern.damage)
print "SwordsMan Damage:  " + str(swordsMan.damage)
print "Archer Damage: " + str(archer.damage)

print "\n"

print "Mage: %s" % (greenLantern.StrongTest())
print "SwordsMan: %s" % (swordsMan.StrongTest())
print "Archer: %s" % (archer.StrongTest())

print "\n"

greenLantern.printName()
swordsMan.printName()
archer.printName()


print "\n\n\t\tNPC's"

class BaseNPC(object):
    def __init__(self, name, gender, age,):
        self.name = name
        self.gender = gender
        self.age = age
        self.weapon = "Bastard Sword"
        self.health = 100
        self.damage = 50
        self.magic = 10
        self.ally = True




class Villager(BaseNPC):
    def __init__(self, name, gender, age):
        super(Villager, self).__init__(name, gender, age)
        self.magic = 5
        self.damage = 10

villager = Villager("Melisa", "Female", 16)
villager1 = Villager("Milton", "Male", 18)
villager2 = Villager("Surten", "Male", 22)

print "\n"

print "Villager Damage: " + str(villager.damage)
print "Villager1 Damage: " + str(villager1.damage)
print "villager2 Damage: " + str(villager2.damage)


print "\n"

print "Village Magic: " + str(villager.magic)
print "VIllager1 Magic: " + str(villager1.magic)
print "Villager2 Magic: " + str(villager2.magic)



print "\n\n\t\tEnemies"

class BaseEnemy(object):
    def __init__(self):
        self.damage = 5
        self.weapon = "Club"

class Orc(BaseEnemy):
    def __init__(self):
        super(Orc,self).__init__()

orc = Orc()

print("\n")

print ("The ORC damage is: " + str(orc.damage))
print ("The ORC Weapon is: " + orc.weapon)
