def add (a, b) :
    return a + b
def subtract (a, b) :
    return a - b
def multiply (a, b) :
    return a * b
def divide (a, b) :
    if a == 0 :
        print("impossible")
    return a / b

print("choose your operation :")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice = input("enter your operation (1/2/3/4) :")
num1 = float(input("enter your first number :"))
num2 = float(input("enter the second number :"))
if choice == "1" :
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == "2" :
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == "3" :
    print(f"{num1} * {num2} = {multiply(num1, num2)} ")
elif choice == "4" :
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else :
    print("invalid, pls try again")