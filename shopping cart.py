fruits = []
meats = []
others = []

while True:
    fruit = input("Input fruit you want to buy (q to quit): ")
    if fruit.lower() == "q":
        break
    else: 
        fruits.append(fruit)
print(fruits)

while True:
    meat = input("Input meat you want to buy (q to quit): ")
    if meat.lower() == "q":
        break
    else: 
        meats.append(meat)
print(meats)

print("-----shopping cart------")
print(f"fruits: {fruits}", end=" ")
print(f"meats: {meats}")