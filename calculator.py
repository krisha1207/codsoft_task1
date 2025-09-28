a = float(input("enter the first number = "))

sign = input("enter the operation (+,-,/,*): ")

b = float(input("enter the second number = "))

if sign == '+':
    print("Addition of the numbers is : ",a+b)

elif sign == '-':
    print("Subtraction of the numbers is : ",a-b)

elif sign == '*':
    print("Multiplication of the numbers is : ",a*b)

elif sign == '/':
 
 if b != 0:
    print("Divison of numbers is : ",a/b)
 else:
    print("error!")

else:
    print("invalid operator")
