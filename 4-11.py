pizzas=['pepperoni','pan','chicken']
friend_pizzas=pizzas[:]
pizzas.append('beef')
friend_pizzas.append('banana')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

