import sys
import default
import spy_status
import spy_friend

#Function to add Menu
def start_chat(spy_name, spy_age, spy_rating):
	current_status_message = None
	show_menu = True

	while show_menu == True:
		menu_choice = input("\n1. Add a Status Update.\n2. Add Friend.\n3. Exit Application.\n")
		print("Enter your choice: ")
		if menu_choice == '1':
			#update the status
			print("You have chosen to add a status")
			current_status_message = spy_status.add_status(current_status_message)
		elif menu_choice == '2':
			print("You have chosen to add a friend")
			spy_friend.add_friend()
		elif menu_choice == '3':
			show_menu = False

#Choice of profile
print("Welcome to SpyChat")
choice = input("Do you want to proceed with default settings or not (Y/N)?: ")

spy = {
	'name' : "",
	'age' : 0,
	'rating' : 0.0,
	'is_online': True
}

if choice.upper() ==  'Y':
	spy['name'] = default.spy['name']
	spy['age'] = default.spy['age']
	spy['rating'] = default.spy['rating']
	spy['is_online'] = default.spy['is_online']
else:
	spy['name'] = input("Enter your name: ")
	spy['age'] = int(input("What is your age?: "))
	spy['rating'] = float(input("What is your rating? (0-5): "))
	spy['is_online'] = True

#Validation of name and age
if spy['name'].isalpha() == False:
	print("Invalid name")
	sys.exit(0)

if spy['age'] <= 12 or spy['age'] >= 50:
	print("Invalid age")
	sys.exit(0)

#Rating of the spy
if spy['rating'] >= 4 or spy['rating'] == 5:
	print("You are an A grade Spy.")
elif spy['rating'] >= 2 or spy['rating'] == 3.9:
	print("You are an B grade Spy.")
elif spy['rating'] >= 1 or spy['rating'] == 2.9:
	print("You are an C grade Spy.")
else:
	print("You have entered an incorrect rating.")
	sys.exit(0)

#Starting Chat
print("\nHello " + spy['name'] + ".")
start_chat(spy['name'], spy['age'], spy['rating'])
