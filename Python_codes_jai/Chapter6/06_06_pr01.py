#Write a program to find greatest among 4 numbers entered by user

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
num4 = int(input("Enter number 4:"))

if(num1>num2):
    f1 = num1
else:
    f1 = num2

if(num3>num4):
    f2 = num3
else:
    f2 = num4

if(f1>f2):
    print(str(f1) + " is Greatest")
else:
    print(str(f2) + " is Greatest")