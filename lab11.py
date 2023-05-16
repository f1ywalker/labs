def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' специализируется на кухне '{self.cuisine_type}'.")

        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")


    newRestaurant = Restaurant("Итальянский дворик", "итальянская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' специализируется на кухне '{self.cuisine_type}'.")

        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")


    restaurant_name = input("Введите название ресторана: ")
    cuisine_type = input("Введите тип кухни: ")
    new_restaurant = Restaurant(restaurant_name, cuisine_type)

    new_restaurant.describe_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' специализируется на кухне '{self.cuisine_type}'.")

        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана '{self.restaurant_name}' обновлен до {self.rating}.")

    restaurant_name = input("Введите название ресторана: ")
    cuisine_type = input("Введите тип кухни: ")
    rating = float(input("Введите начальный рейтинг ресторана: "))
    new_restaurant = Restaurant(restaurant_name, cuisine_type, rating)

    new_restaurant.describe_restaurant()

    new_rating = float(input("Введите новый рейтинг ресторана: "))
    new_restaurant.update_rating(new_rating)
z1(), z2(), z3()