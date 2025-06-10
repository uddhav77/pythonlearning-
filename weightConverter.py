weight = float(input("Enter your weight : "))
unit = input("Enter unit in kilograms or pound (K or P) : ")

if unit == "K":
    weight = weight * 2.205
    print(f"Your weight is {round(weight, 2)} lbs.")
elif unit == "P":
    weight = weight / 2.205
    print(f"Your weight is {round(weight, 2)} kgs.")
else:
    print("Enter a valid unit")