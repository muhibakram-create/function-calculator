try:
    num1 = float(input("What is the 1st number?"))
    num2 = float(input("What is the 2nd number?"))
    ZeroDivision1 = num1/num2
    ZeroDivision1 = num2/num1
except ValueError:
    print("Please enter a proper number.")
except ZeroDivisionError:
    print("There is a zerodivision error")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("The sum is:", add(num1,num2))
print("The subtracted result is:", subtract(num1,num2))
print("The quotient is:", divide(num1,num2))
print("The product is:", multiply(num1,num2))
