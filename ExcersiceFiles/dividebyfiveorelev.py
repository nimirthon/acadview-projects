# program to check whether a number is divisible by 5 or 11 or not

print ("Enter a number: ")
numbr = int(input())
if numbr % 5 == 0 or numbr % 11 == 0:
    print ("The number is divisible by 5 and 11.")
else:
    print ("The number is NOT divisible by 5 and 11.")
