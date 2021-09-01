class Restaurant():
    """a simple effort for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is opening.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("big brother", "hot pot")
print(restaurant.number_served)

restaurant.number_served = 30
print(restaurant.number_served)

restaurant.set_number_served(39)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)
