def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = []

        def display_flavors(self):
            print("Доступные вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

    ice_cream_stand = IceCreamStand("Мороженое на углу", "Кафе-мороженное")
    ice_cream_stand.flavors = ["Шоколад", "Ваниль", "Клубника", "Манго"]

    ice_cream_stand.display_flavors()
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine_type, flavors, location, hours):
            super().__init__(name, cuisine_type)
            self.flavors = flavors
            self.location = location
            self.hours = hours

        def show_flavors(self):
            print("У нас есть такие разновидности мороженного:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        def show_hours(self):
            print("Кафе открыто:")
            for hours in self.hours:
                print(f" {hours}")

        def show_location(self):
            print("Кафе находится:")
            for location in self.location:
                print(f" {location}")

        def add_flavor(self, new_flavor):
            self.flavors.append(new_flavor)
            print(f"{new_flavor} был добавлен(а)!")

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} был(а) удален!")
            else:
                print(f"{flavor} нет в меню.")

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"Да, у нас есть {flavor}!")
            else:
                print(f"Извините, у нас нет {flavor}.")

        def show_menu(self, menu_type):
            if menu_type == "На палочке":
                print("У нас есть следующие вкусы мороженого на палочке:")
                for flavor in [input("введите вкус:"), input("введите вкус:"), input("введите вкус:")]:
                    print(f"- {flavor}")
            elif menu_type == "Мягкое мороженное":
                print("У нас есть следующие вкусы мягкого мороженного:")
                for flavor in [input("введите вкус:"), input("введите вкус:"), input("введите вкус:")]:
                    print(f"- {flavor}")

    my_ice_cream_stand = IceCreamStand("Сладкие угощения", "кафе-мороженое",
                                       [input("введите вкус:"), input("введите вкус:"), input("введите вкус:")],
                                       ["Большая морская"], ["10:00–22:00"])

    my_ice_cream_stand.add_flavor(input("какой вкус добавить - "))
    print()
    my_ice_cream_stand.show_flavors()
    print()
    my_ice_cream_stand.remove_flavor(input("удалить вкус -"))
    my_ice_cream_stand.check_flavor(input("проверить вкус -"))
    my_ice_cream_stand.show_menu(input("проверить тип - "))
    print()
    my_ice_cream_stand.show_hours()
    print()
    my_ice_cream_stand.show_location()

def z2():
    import tkinter as tk

    class IceCreamStand:
        def __init__(self, restaurant_name, cuisine_type, flavors):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.flavors = flavors

        def display_flavors(self):
            print("Available ice cream flavors:")
            for flavor in self.flavors:
                print(flavor)

    ice_cream_stand = IceCreamStand("Мороженое на углу", "Кафе-мороженое", ["Шоколад", "Ваниль", "Клубника", "Манго"])


    root = tk.Tk()
    root.title("Меню кафе-мороженого")

    def show_flavors():
        flavors = "\n".join(ice_cream_stand.flavors)
        flavors_label.config(text=flavors)

    restaurant_name_label = tk.Label(root, text="Название: " + ice_cream_stand.restaurant_name)
    restaurant_name_label.pack()

    cuisine_type_label = tk.Label(root, text="Тип кухни: " + ice_cream_stand.cuisine_type)
    cuisine_type_label.pack()

    flavors_label = tk.Label(root, text="Сорта мороженого:")
    flavors_label.pack()

    show_flavors_button = tk.Button(root, text="Показать сорта", command=show_flavors)
    show_flavors_button.pack()

    root.mainloop()
z1(),z2()