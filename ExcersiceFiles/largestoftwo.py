# program to find maximum between two numbers

print ("Enter any two numbers: ")
num1 = int(input())
num2 = int(input())
flag = 0
if num1 > num2:
    maximum = num1
    flag = 1
elif num1 < num2:
    maximum = num2
    flag = 1
else:
    print("Both the numbers are equal.")
if flag == 1:
    print ("Largest from the given two numbers is: ", maximum)
