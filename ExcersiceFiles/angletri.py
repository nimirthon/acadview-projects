# program to input angles of a triangle and check whether triangle is valid or not

ang1 = int(input("Enter the degree of the first angle: "))
ang2 = int(input("Enter the degree of the second angle: "))
ang3 = int(input("Enter the degree of the third angle: "))

if ang1 + ang2 + ang3 == 180:
    print ("It is a Triangle.")
else:
    print ("It is NOT a Triangle.")
