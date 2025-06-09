operator = input("Enter the operation ( + - * / ) : ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+" :
    sum = num1 + num2
    print(f"The sum is {sum}")
elif operator == "-" :
    diff = num1 - num2
    print(f"The diff is {diff}")
elif operator == "*" :
    product = num1 * num2
    print(f"The product is {product}")
elif operator == "/" :
    div = num1 / num2
    print(f"The division is {div}")
    