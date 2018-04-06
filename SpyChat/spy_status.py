import sys
import spy_friend
from spy_details import SPY, ChatMessage
import csv

#Mod5: Status Update.
#Function to add Status Message
STATUS_MESSAGE = []
def add_status(current_status_message):
	#Prints the current Status
	if current_status_message == None:
		print("Current Status is empty.")
	else:
		print("Your current Status is: " + current_status_message)
	#Option for the user to choose between an older Status or enter a new Status
	update_choice = input("Do you want to select from an older status (y/n)?: ")
	if update_choice.upper() == 'N':
		new_status_message = input("Enter the new status message: ")
		#Validate whether the status is not empty and then add the new Status
		if len(new_status_message) > 0:
			updated_status_message = new_status_message
			STATUS_MESSAGE.append(updated_status_message)

	elif update_choice.upper() == 'Y':
		for i in range(len(STATUS_MESSAGE)):
			print(str(i+1) + " " + STATUS_MESSAGE[i])

		message_selection = int(input("Choose a Status from the older messages."))
		if len(STATUS_MESSAGE) > message_selection:
			updated_status_message = STATUS_MESSAGE[message_selection-1]

	return updated_status_message

#function to load the Status from the CSV file status.csv
def load_status():
	read_object = open("status.csv", 'r')
	reader = csv.reader(read_object)
	for row in reader:
		if row:
			STATUS_MESSAGE.append(row[0])
	read_object.close()
	if len(STATUS_MESSAGE) > 0:
		return STATUS_MESSAGE[-1]
	else:
		return None

#Mod8: Save to file status.csv
#function to save the Status in the CSV file status.csv
def save_status():
	write_object = open("status.csv", 'w')
	writer = csv.writer(write_object)
	for i in range(len(STATUS_MESSAGE)):
		if i:
			writer.writerow([STATUS_MESSAGE[i]])
	write_object.close()
