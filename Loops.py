# while loop

count = 0
while count < 3:
    #    print("Hello world")
    print(count)
    count = count + 1

print("-------------------------")

i = int(input("Please input number"))
while i < 10:
    print(i)
    i = i + 1
else:
    print("Value out of range")
print("-------------------------")

# For Loop

name = ["Allan", "Albert", "Julian", "Joan"]
for i in name:
    print(i)

print("-------------------------")

str = "I love Python"
for i in str:
    print(i)
print("-------------------------")
# Iteration by index of sequence

# for loop with else
name = ["Mea", "Official", "Limited"]
for index in range(len(name)):
    print(name[index])
else:
    print("Name List is over")
print("-------------------------")

districts = ["Mubende", "Hoima", "Kiboga", "Mabale", "Mbarara"]
for index in range(3):
    print(districts[index])
else:
    print("Districts list complete")

# Nested for loop

for i in range(1, 5):
    for j in range(i):
        print(i, end='')
    print()
