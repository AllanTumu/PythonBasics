# Calling a function

# parameterized function


def test():
    print("Hello World")


test()


# non Parameterised function


def sum(a):
    print(a + 30)


sum(20)


# Optional/default parameters

def get_country_name(name="Uganda"):
    print(name)


get_country_name()
get_country_name("Kenya")


# Pass a list to a function

def get_names(list):
    for x in list:
        print(x)


names = ["Allan", "Rob", "Frank", "Edward"]
get_names(names)


# function with return

def addition(a, b):
    return a + b


c = addition(10, 20)
print(c)

print("-------------------------------------------------")


def get_capital_name(country_name):
    if country_name == "Uganda":
        return "Kampala"
    elif country_name == "Kenya":
        return "Nairobi"
    elif country_name == "Tanzania":
        return "Dar-e -salam"


print(get_capital_name("Uganda"))
print("-------------------------------------------------")


def launch_browser(browser_name):
    if browser_name == "Chrome":
        print("Launching Chrome Browser")
    elif browser_name == "Firefox":
        print("Launching Firefox Browser")
    else:
        print("No Browser defined")


browser = input("Which Browser are you using?")
launch_browser(browser)


# Recursion in Python
# A recursive function is a function calling its self

# WAP to get factorial of a given Number
# fact(4) =  4*3*2*1 = 24

def factorial(number):
    if number > 1:
        number = number * factorial(number - 1)
    return number


x = int(input("Please input the number greater than 1"))
print(factorial(x))


def login(user_name, password):
    print("login with %s and %s " % (user_name, password))


login("mea@gmail.com", "test@123")
