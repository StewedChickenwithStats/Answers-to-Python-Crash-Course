favorite_places={
	'lily':['china','america'],
	'mike':['japan'],
	'linda':['japan','canada'],
	}

for name, places in favorite_places.items():
	print("\n"+name.title()+"'s favorite places are:")
	for place in places:
		print("\t"+place.title())
