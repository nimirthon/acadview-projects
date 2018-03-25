import sys
import default

#Function to add Menu
def start_chat(spy_name, spy_salutation, spy_age, spy_rating):
	current_status_message = None
	show_menu = True
	while (show_menu):
		menu_choice = input("\n1. Add a status update. \n2. Close Application.\n")
		if menu_choice == 1:
			print('You have chosen to update the status.')
			current_status_message = add_status(current_status_message)
		elif menu_choice == 2:
			show_menu = False

#Function to add Status Message
STATUS_MESSAGES = []
def add_status(current_status_message):
	if (current_status_message != None):
		print("Your current status message is " +current_status_message+ "\n")
	else:
		print("You don't have any status message currently")
	update_choice = input("Do you want to select from the older status (y/n)?")
	if update_choice.upper() == "N":
		new_status_message = input("What status message do you want to be set?")
		if len(new_status_message) > 0:
			updated_status_message = new_status_message
			STATUS_MESSAGES.append(updated_status_message)
		elif update_choice.upper() == 'Y':
			item_position = 1
		for message in STATUS_MESSAGES:
			print (item_position + ". " + message)
		item_position = item_position + 1
		message_selection = input("\nChoose from the above messages ")
		if len(STATUS_MESSAGES) >= message_selection:
			updated_status_message = STATUS_MESSAGES[message_selection - 1]
	return updated_status_message

#function to add Friend
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []
def add_friend():
	new_name = input("Please add your friend's name:")
	new_salutation = input("Are they Mr. or Ms.?: ")
	new_name = new_name + " " + new_salutation
	new_age = input("Age?")
	new_rating = input("Spy rating?")

#Validate Name and Age
if new_name.isalpha() == True and new_age > 12 and new_rating >= spy_rating:
	friends_name.append(new_name)
	friends_age.append(new_age)
	friends_rating.append(new_rating)
	friends_is_online.append(True)
else:
	print("Sorry! Invalid entry.")

#Choice of profile
print("Welcome to SpyChat")
menu_choice = input("Do you want to proceed with default settings or not?.\nEnter Y for Yes or N for No: ")
if menu_choice.upper() ==  'Y':
	spy_name = default.spy_name
	spy_salutation = default.spy_salutation
	spy_age = default.spy_age
	spy_rating = default.spy_rating
elif menu_choice.upper() ==  'N':
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
print("hello %s %s" % (spy_salutation, spy_name))
print("Your age is %s" % (spy_age))
print("Your rating is %s" % (spy_rating))

#Menu called
start_chat(spy_name, spy_salutation, spy_age, spy_rating)
