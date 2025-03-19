x = input("Name: ")
weight = input("weight: ")
unit = input("unit: ")
if unit == "lb":
    b = float(weight) * 0.45
    print(f" {x} you weight in kg: {b}")
elif unit == "kg":
    b = float(weight) / 0.45
    print(f" {x} you weight in lb: {b}")
else:
    print(f" unit error")
    