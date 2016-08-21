class Parent(object):

    def override(self, PR):
        print ("%s override()") % (PR)

    def implicit(self):
        print ("PARENT implicit()")

    def altered(self):
        print("PARENT altered")

dad = Parent()
#son = Child()

dad.implicit()
#son.implicit()

dad.override("Parent")
#son.override()

dad.altered()
#son.altered()
