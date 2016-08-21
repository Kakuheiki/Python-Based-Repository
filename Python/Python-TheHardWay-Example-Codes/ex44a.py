class Parent(object):

    def implicit(self):
        print ("Parent implicit()")
        print ("Fuck you")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
