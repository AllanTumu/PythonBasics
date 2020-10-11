x = int(input("Please enter the value of X"))

if x < 0:
    print("x is a negative number")
elif x > 0:
    print("x is a positive number")
else:
    print("x is undefined")

print("************************************")

# dead code
# In this case the else statement will never be executed

if True:
    print("Pass")
else:
    print("Fail")

print("************************************")

# Comparison in If statements

a = 100
b = 200
c = 300

if a > b and a > c:
    print("a is the highest number")
elif b > c:
    print("b is the highest number")
else:
    print("c is the highest number")

print("************************************")

# Calculating total Salary

total_salary_earned = int(input("Please input your total salary"))
if total_salary_earned < 1000:
    total_salary_earned = total_salary_earned + 200
elif 1000 < total_salary_earned <= 5000:
    total_salary_earned = total_salary_earned + 500
else:
    total_salary_earned = total_salary_earned * 2


# Different ways to concatenate strings with integers in python

# 1
print("Your total salary earned is", total_salary_earned)
print("************************************")
# 2 (str method)
print("Your total salary earned is", str(total_salary_earned))
print("************************************")
# 3 (f strings)
print(f'{"Your total salary earned is "}{total_salary_earned}')



