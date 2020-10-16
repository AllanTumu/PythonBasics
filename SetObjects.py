# Set doesn't store the value in form of indexing
# It is not Order based
# It stores multiple data types
# It performs different mathematical operations
# it doesn't store duplicated values
# To define a set , we use {}

set1 = {100, "Tom", 23.56, True}
print(set1)

set2 = {1, 2, 1, 2, 3, 1, 2, 3}
print(set2)  # Repeated values are eliminated

# set() function
set3 = set("python")
print(set3)

set4 = set([10, 20, 30, 40, 50])
print(set4)

# While creating a set object, you can store only Numbers, Strings, tuple
# list and dictionary objects are not allowed

set1 = {(10, 20, 30, 40), 50, 60}
print(set1)

# set operations
# Union: (it is denoted by |)
p1 = {1, 2, 3, 4, 5, 6, 9, 4}
p2 = {6, 7, 8, 9, 10}

print(p1 | p2)  # | --> represents Union
print(p1.union(p2))  # Union can also be used to combine two sets

# Intersection operator (it is denoted by &)
print(p1 & p2)
print(p1.intersection(p2))

# Difference of 2 sets. Difference is denoted by -
print(p1 - p2)
print(p2 - p1)
print(p1.difference(p2))

# Symmetric difference
# Difference of all the sets minus common elements

print(p1 ^ p2)
print(p1.symmetric_difference(p2))

# Set  In built methods

# 1. add ():

s1 = {"Java", "Python", "C++"}
s1.add("Perl")
print(s1)

# 2. update()
s3 = {"Java", "Python", "C++"}
s3.update(["C", "VisualBasic"])
print(s3)

# 3. clear():
s3.clear()
print(s3)

# 4. copy():
lang = {"java", "Python", "C++"}
lang1 = lang.copy()
print(lang1)

