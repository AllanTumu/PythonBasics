class Base1(object):
    def __init__(self):
        self.str1 = "Allan"
        print("Base 1")


class Base2(object):
    def __init__(self):
        self.str2 = "Aron"
        print("Base 2")


# Multiple inheritance is allowed in Python
class Child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Child")

    def printStrings(self):
        print(self.str1, self.str2)


ob = Child()
ob.printStrings()
