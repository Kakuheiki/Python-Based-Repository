class Hero:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.weapon = "Katana"
        self.health = 100

    def Charapter(self):
        print("\nMy name is %s, I'm a %s, I'm %s YO, I can kill you with my %s") % \
        (self.name, self.gender, self.age, self.weapon,)

    def Eat(self, foot):
        if (foot == "Apple"):
            self.health -= 10
        elif (foot == "Ham"):
            self.health += 10



a = "Gilbert"
b = "Man"
c = "15"
d = raw_input("\nWhat you wanna eat? ")

Gilbert = Hero(a, b, c)
print Gilbert.Eat(d)

Gilbert.Charapter()


if d == "Ham":
    Gilbert.Eat(d)


elif d == "Apple":
    Gilbert.Eat(d)

else:
    print ("\n0 %s in stock" % (d))


print ("\t")
print ("\nHealth: " + str(Gilbert.health))
