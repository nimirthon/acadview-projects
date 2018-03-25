#Function to add Status Message
STATUS_MESSAGE = []
def add_status(current_status_message):
	if current_status_message == None:
		print("Current Status is empty.")
	else:
		print("Your current status is: " + current_status_message)

	update_choice = input("Do you want to select from an older status (y/n)?: ")
	if update_choice.upper() == 'N':
		new_status_message = input("Enter the new status message: ")

		if len(new_status_message) > 0:
			updated_status_message = new_status_message
			STATUS_MESSAGE.append(updated_status_message)

	elif update_choice.upper() == 'Y':
		for i in range(len(STATUS_MESSAGE)):
			print(str(i+1) + " " + STATUS_MESSAGE[i])

		message_selection = int(input("Choose a status from the older messages."))
		if len(STATUS_MESSAGE) > message_selection:
			updated_status_message = STATUS_MESSAGE[message_selection-1]

	return updated_status_message
