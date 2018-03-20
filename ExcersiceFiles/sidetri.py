# program to input all sides of a triangle and check whether triangle is valid or not

a = int(input("Enter the side a of Triangle: "))
b = int(input("Enter the side b of Triangle: "))
c = int(input("Enter the side c of Triangle: "))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print ("It is NOT a Triangle.")
else:
    print ("It is a Triangle.")
