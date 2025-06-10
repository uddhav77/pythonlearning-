operator = input("Enter the operation ( + - * / ) : ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+" :
    sum = num1 + num2
    print(f"The sum is {round(sum, 3)}")
elif operator == "-" :
    diff = num1 - num2
    print(f"The diff is {round(diff, 3)}")
elif operator == "*" :
    product = num1 * num2
    print(f"The product is {round(product, 3)}")
elif operator == "/" :
    div = num1 / num2
    print(f"The division is {round(div, 3)}")
else:
    print("Please enter a valid operation.")

    