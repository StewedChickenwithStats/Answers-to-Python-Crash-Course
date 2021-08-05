current_users=['Lily','Anna','Linda','Kim','Zoe']
new_users=['Lily','Anna','Sue','Mike','Chen']

for new_user in new_users:
	if new_user.title() in current_users or new_user.lower() in current_users or new_user.upper() in current_users:#ignore case
		print("Sorry, you should enter another user name.")
	else:
		print("This user name is not used by others.")