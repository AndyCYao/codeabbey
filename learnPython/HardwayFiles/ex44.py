class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()  # calls own implicit
son.implicit()  # calls parent's implicit

dad.override()  # calls own override
son.override()  # calls own over ride

dad.altered()  # calls own altered
son.altered()  # calls own altered, then calls parents altered,
