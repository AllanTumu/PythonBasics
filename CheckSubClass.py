class Base(object):
    pass  # Empty class


class Child(Base):
    pass  # Empty class


# Test Code
print(issubclass(Child, Base))
print(issubclass(Base, Child))

c = Child()
b = Base()

print(isinstance(b, Child))
print(isinstance(c, Child))
print(isinstance(c, Base)) # Base class can be referred by base class instance and Child class instance
