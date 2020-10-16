# Tuple : Is a collection of elements of any data types
# Tuple Vs list
# 1. Syntax: You have to store the values in a tuple with (), but in List: []
# 2. Tuple is Immutable(can't change any value in tuple) but List is mutable (Can change value in list)

names = ("Java", "Python", "java Script", "C-sharp")
marks = (100, 20, 30, 40, 80)
employeeData = ("Tom", 24, 'm', 23.33, True)

print(employeeData)
print(employeeData[3])

# Going beyond the index it will throw an out of range exception

# Backwards index
print(employeeData[-5])

# Mutability
list = [12, 20, 30, 40, 50]
list[0] = 10
print(list)

# tuple concatenation
t1 = (1, 2, 3, 4, ".")
t2 = (5, 6, 7, 8)
print(t1 + t2)

# repetition
print(t2 * 2)

# Range Slicing
t4 = (1, 2, 3, 4, 5)
print(t4[1:3])

# in:
employeeData1 = ("Tom", 24, 'm', 23.33, True)
print(25 in employeeData1)
print(24 in employeeData1)

# not in:
print(35 not in employeeData1)

# length
length = len(employeeData1)
print(length)

# max number
number = (10, 20, 30, 40, 50, 60)
print(max(number))

names1 = ("Java", "Python", "java Script", "C-sharp")
print(max(names1))
print(min(names1))

