import sys
import csv
from spy_details import SPY, ChatMessage

#Mod4: Add a Spy.
#function to add Friend
friends = []
def add_friend():
	friend_name = input("What is your friend's name?: ")
	friend_salutation = input("Salutation? (Mr./ Mrs.): ")
	friend_age = int(input("Age? "))
	friend_rating = float(input("Rating? "))

	#Validation of the friend's name and age
	if friend_name.isalpha() == False:
		print("\nThe name entered is invalid.\nThe Application is being Terminated.")
		sys.exit(0)

	if friend_age <= 12 or friend_age >= 50:
		print("\nThe age entered is invalid.\nThe Application is being Terminated.")
		sys.exit(0)
	#Adding the new friend to the list
	new_friend = SPY(friend_name, friend_salutation, friend_age, friend_rating)
	friends.append(new_friend)
	#Printing the list of friends after addind the new friend
	print("Below is an updated list of friends.")
	counter = 0
	for f in friends:
		counter += 1
		print('%d. %s' % (counter, f.name))

#function to select Friend
def select_friend():

	#Printing the list of friends of the user
	counter = 0
	for f in friends:
		counter += 1
		print('%d. %s' % (counter, f.name))

	#Asking the user to select a friend
	friend_choice = int(input("\nSelect a friend from the list: "))
	friend_choice -= 1

	#Returning the index
	return friend_choice

#Mod5: Send a Message.
#function to send a message to Friend
def send_message():
	print("\nSelect a friend from the list to whom you want to send the message.")
	friend_choice = select_friend()
	#The Message
	message = input("Enter the message to be send: ")
	new_chat_message = ChatMessage(message, True)
	#Confirmation
	friends[friend_choice].chats.append(new_chat_message)
	print("Your message has been sent to %s." %friends[friend_choice].name)

#Mod6: Read a Message.
#function to read a message that has been sent to a Friend
def read_message():
	print("\nSelect a friend from the list whose message you want to be read.")
	sender = select_friend()
	#Validates the Message and then prints it
	if len(friends[sender].chats) == 0:
		print("You have no conversation with %s." %friends[sender].name)
	else:
		for i in range(len(friends[sender].chats)):
			print(friends[sender].chats[i].message)

#function to load Friends from the CSV file friends.csv
def load_friends():
	read_object = open("friends.csv", 'r')
	reader = csv.reader(read_object)
	for row in reader:
		if row:
			name = row[0]
			salutation = row[1]
			age = int(row[2])
			rating = float(row[3])
			is_online = bool(row[4])
			new_friend = SPY(name, salutation, age, rating)
			friends.append(new_friend)
	read_object.close()

#Mod8: Save to file friends.csv
#function to save Friends in the CSV file friends.csv
def save_friends():
	write_object = open("friends.csv", 'w')
	writer = csv.writer(write_object)
	for i in range(len(friends)):
		if friends:
			name = friends[i].name
			salutation = friends[i].salutation
			age = friends[i].age
			rating = friends[i].rating
			is_online = friends[i].is_online
			writer.writerow([name,salutation,age,rating,is_online])
	write_object.close()
