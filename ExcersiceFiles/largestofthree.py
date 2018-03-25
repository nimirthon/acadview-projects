# program to find maximum between three numbers

print ("Enter any three numbers: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
flag = 0
if num1 > num2 and num1 > num3:
    maximum = num1
    flag = 1
elif num1 < num2 and num3 < num2:
    maximum = num2
    flag = 1
elif num1 < num3 and num2 < num3:
    maximum = num3
    flag = 1
else:
    print("All the numbers are equal.")
if flag == 1:
    print ("Largest from the given three numbers is: ", maximum)
