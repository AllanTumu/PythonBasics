def login(username, password):
    print(username, password)


login("Allan", "123")


# *arg

def get_max(*arg):
    for x in arg:
        print(x)


get_max(10, 20, 30, 40, 50, 60, 70)
get_max("a", "b", "c")


# keyWord args
# **arg

def get_student_marks(**args):
    for key, value in args.items():
        print("%s == %s" % (key, value))


get_student_marks(Allan=10, tom=20, Petero=30)

# lambda functions: Anonymous functions
# lambda functions are functions without a name:

cube = lambda x: x * x * x

print(cube(3))


total = lambda marks: marks+30
print(total(100))
