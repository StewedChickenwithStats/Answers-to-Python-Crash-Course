rivers={'nile':'egypt','yangtze river':'china','lena river':'russia'}

for river, state in rivers.items():
	print("The "+river.title()+" runs through "+state.title()+'.')

for river in rivers.keys():
	print(river.title())

for state in rivers.values():
	print(state.title())