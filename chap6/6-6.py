favorite_languages={
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

check_lists=['jen','phil']

for name in favorite_languages.keys():
	if name in check_lists:
		print("Thanks "+name.title()+"!")
	else:
		print("Hi "+name.title()+","+"please complete this investigation quickly!")
