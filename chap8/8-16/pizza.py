def make_pizza(size, *toppings):
    """describe the pizza you want to make"""
    print("\nMaking a" + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
