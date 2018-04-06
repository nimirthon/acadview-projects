import sys
import spy_status
from spy_details import SPY
import spy_friend

print("Welcome to SpyChat.")

#Mod1: Creating the User Profile
#Option to proceed with default values or enter new values
print("Let's first create your profile.\n")
profile_choice = input("Do you want to proceed with default settings or not (Y/N)?: ")

if profile_choice.upper() == 'Y':
	spy = SPY("Bond", "Mr.", 35, 4.8)
else :
	name = input("Enter your name: ")
	salutation = input("Salutation? (Mr./ Mrs.): ")
	age = int(input("What is your age?: "))
	rating = float(input("What is your rating? (0-5): "))

	#Validation of the user's name and age
	if name.isalpha() == False:
		print("\nGiven name is invalid.\nTerminating application")
		sys.exit(0)

	if age <= 12 or age >= 50:
		print("\nGiven age is invalid.\nTerminating application")
		sys.exit(0)

	#Rating of the spy
	if rating >= 4 or rating == 5:
		print("You are an A grade Spy.")
	elif rating >= 2 or rating == 3.9:
		print("You are an B grade Spy.")
	elif rating >= 1 or rating == 2.9:
		print("You are an C grade Spy.")
	else:
		print("You have entered an incorrect rating.")
		sys.exit(0)

	spy = SPY(name, salutation, age, rating)

#Printing the details of the Spy
print("\nHello %s %s " %(spy.salutation, spy.name))
print("We have successfully created your account.")


#Mod2: Creating a menu.
#function menu
def start_chat():
	show_menu = True
	while show_menu:
		print("\nYou can choose from the below Operations.")
		print("1. Add Friend\n2. Add Status\n3. Send a Message\n4. Read a Message\n5. Close application")
		menu_choice = int(input("What would your choice be: "))

		if menu_choice == 1:
			print("\nYou have chosen to add a Friend.")
			spy_friend.add_friend()
		elif menu_choice == 2:
			print("\nYou have chosen to update your Status.")
			spy.current_status_message = spy_status.add_status(spy.current_status_message)
		elif menu_choice == 3:
			print("\nYou have chosen to send a Message to a Friend.")
			spy_friend.send_message()
		elif menu_choice == 4:
			print("\nYou have chosen to read a Message from a Friend.")
			spy_friend.read_message()
		elif menu_choice == 5:
			print("\nYou have chosen to terminate the application.")
			show_menu = False
		else:
			print("\nInvalid choice entered.")

spy_friend.load_friends()
spy.current_status_message = spy_status.load_status()
start_chat()
spy_friend.save_friends()
spy_status.save_status()
