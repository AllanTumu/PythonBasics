class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployed(self):
        return False


class Employee(Person):
    def isEmployed(self):
        return True


# Test Person

emp = Person("Allan")
print(emp.name)
print(emp.getName(), emp.isEmployed())

emp1 = Employee("Tom")
print(emp1.name)
print(emp1.getName())
print(emp1.isEmployed()) # This will return true because the isEmployed function is already over ridden
