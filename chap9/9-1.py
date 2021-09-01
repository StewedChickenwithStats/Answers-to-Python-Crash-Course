class Restaurant():
    """a simple effort for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is opening.")


restaurant = Restaurant("big brother", "hot pot")
restaurant.describe_restaurant()
restaurant.open_restaurant()
