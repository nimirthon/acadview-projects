import sys
import default
print("Welcome to spychat")
choice = input("Enter 1 if you want to have default settings: ")
if choice == '1':
	spy_name = default.spy_name
	spy_salutation = default.spy_salutation
	spy_age = default.spy_age
	spy_rating = default.spy_rating
else:
	spy_name = input("Enter your Name: ")
	spy_salutation = input("Enter your Salutation (Mr. or Mrs.): ")
	spy_age = input("Enter your age: ")
	spy_rating = input("Enter your rating: ")

#Validating the name of the spy
if spy_name.isalpha() == False:
	print("Name is Invalid")
	sys.exit(0)

#Validating the age of the spy
if int(spy_age) <= 12:
	print("Age below 12")
	sys.exit(0)
elif int(spy_age) >= 50:
	print("Age above 50")
	sys.exit(0)

#Rating of the spy
if spy_rating == 'A':
	print("You are a 3 star spy")
elif spy_rating == 'B':
	print("You are a 2 star spy")
elif spy_rating == 'C':
	print("You are a 1 star spy")
else:
	print("You have entered incorrect rating")
	sys.exit(0)

#Printing the result
print("hello " + spy_salutation + spy_name)
print("Your age is " + spy_age)
print("Your rating is " + spy_rating)
