# animal is an object
class Animal(object):
    pass

# dog is an animal


class Dog(Animal):

    def __init__(self, name):
        # dog has a name
        self.name = name


class Cat(Animal):

    def __init__(self, name):
        # cat also have names
        self.name = name


# person are objects
class Person(object):

    def __init__(self, name):
        ##person have names
        self.name = name
        # person have pets of some kind
        self.pet = None


# Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        # when an employee is initialize. it also
        # init. the class above it??
        # super(Employee, self).__init__(name)
        super().__init__()
        # employess have salary
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")
frank = Employee("Frank", 120000)
frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

