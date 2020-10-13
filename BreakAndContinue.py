name = "Tumuhimbise"

# using the break Key word
for i in name:
    print(i)
    if i == "h":
        break

print("----------------------")

# using the continue Key word
for i in name:
    print(i)
    if i == "h":
        continue

print("----------------------")

# using break and continue for lists

str = ["python", "Java", ".net", "C#"]
for i in str:
    print(i)
    if i == ".net":
        break

print("----------------------")
districts = ["Mbarara", "Kampala", "Mbale", "Iganga", "Bududa", "Kyenjojo"]
for d in range(len(districts)):
    print(districts[d])
    if districts[d] == "Mbale":
        break
