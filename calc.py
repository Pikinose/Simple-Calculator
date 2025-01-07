num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number"))
opt = str(input("Enter the operator-> +, -, x, /: "))


def mycalc():
    if opt == "+":
        print(num1+num2)
    elif opt == "-":
        print(num1-num2)
    elif opt == "*":
        print(num1*num2)
    elif opt=="/":
        print(num1/num2)
mycalc()
print("Thanks for using our PIKINOSE console calculator")

