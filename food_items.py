from restaurant import Restaurant


class Food(Restaurant):
    def __init__(self):
        super().__init__()
        self.all_dishes = {}

    def add_items_to_menu(self, restaurant_name, no_of_dishes):
        for j in range(int(no_of_dishes)):
            dish = {}
            print(f"Type Dish {j + 1} Details: ")
            dish_name = input("Name: ").lower()

            if dish_name == "" or dish_name == "none" or dish_name == "null":
                dish_name = input(
                    "Invalid dish name.. please type again: ").lower()
                if dish_name == "" or dish_name == "none"\
                        or dish_name == "null":
                    break

            cost = abs(int(input("Cost: ")))
            time = abs(int(input("Process Time in Minutes: ")))
            dish["dish_name"] = dish_name
            dish["price"] = cost
            dish["process_time"] = time
            dish["restaurant_name"] = restaurant_name

            if "menu" not in self.restaurants[restaurant_name]:
                self.restaurants[restaurant_name]["menu"] = []
                self.restaurants[restaurant_name]["menu"].append(dish)
            else:
                self.restaurants[restaurant_name]["menu"].append(dish)

            if dish_name in self.all_dishes:
                self.all_dishes[dish_name].append(dish)
            else:
                self.all_dishes[dish_name] = []
                self.all_dishes[dish_name].append(dish)

        print("All Restaurants: ", self.restaurants)
        print("All Dishes: ", self.all_dishes)

    def remove_items_from_menu(self, restaurant_name):
        try:
            dish_name = input(
                "Which dish you want to delete" +
                f" from {restaurant_name}: ").lower()

            if dish_name == "" or dish_name == "none" or dish_name == "null":
                dish_name = input(
                    "Invalid dish name.. please type again: ").lower()

            selected_restaurant_menu = self\
                .restaurants[restaurant_name]["menu"]

            for i in range(len(selected_restaurant_menu)):
                if selected_restaurant_menu[i]["dish_name"] == dish_name:
                    del_dish = selected_restaurant_menu.pop(i)
                    print("Dish deleted:", del_dish)
                    break

            if del_dish:
                print("All Restaurants: ", self.restaurants)

            for key in self.all_dishes:
                if key == dish_name:
                    for i in range(len(self.all_dishes[dish_name])):
                        if self.all_dishes[dish_name][i]["restaurant_name"] ==\
                                restaurant_name:
                            del_in_dishes = self.all_dishes[dish_name].pop(i)
                            break

            if del_in_dishes:
                print("All Dishes: ", self.all_dishes)

        except UnboundLocalError:
            print(
                "Error: Invalid input.. dish name does not exist!!")

    def update_price(self, restaurant_name, dish_name, updated_price):
        selected_restaurant_menu = self.restaurants[restaurant_name]["menu"]

        for i in range(len(selected_restaurant_menu)):
            if selected_restaurant_menu[i]["dish_name"] == dish_name:
                selected_restaurant_menu[i]["price"] = updated_price

        print("All Restaurants: ", self.restaurants)

        for key in self.all_dishes:
            if key == dish_name:
                for i in range(len(self.all_dishes[dish_name])):
                    if restaurant_name == self.\
                            all_dishes[dish_name][i]["restaurant_name"]:
                        self.all_dishes[dish_name][i]["price"] = updated_price

        print("All Dishes: ", self.all_dishes)

    def update_process_time(self, restaurant_name,
                            dish_name, updated_process_time):
        selected_restaurant_menu = self.restaurants[restaurant_name]["menu"]

        for i in range(len(selected_restaurant_menu)):
            if selected_restaurant_menu[i]["dish_name"] == dish_name:
                selected_restaurant_menu[i]["process_time"] = int(
                    updated_process_time)

        print("All Restaurants: ", self.restaurants)

        for key in self.all_dishes:
            if key == dish_name:
                for i in range(len(self.all_dishes[dish_name])):
                    if restaurant_name == self.\
                            all_dishes[dish_name][i]["restaurant_name"]:
                        self.all_dishes[dish_name][i]["process_time"] = int(
                            updated_process_time)

        print("All Dishes: ", self.all_dishes)

    def print_menu(self, restaurant_name):
        selected_restaurant_menu = self.restaurants[restaurant_name]["menu"]
        print(
            f"**************** Menu of {restaurant_name} *******************")
        for i in range(len(selected_restaurant_menu)):
            print(
                f"({i + 1})  {selected_restaurant_menu[i]['dish_name']}...." +
                f"...... {selected_restaurant_menu[i]['price']}" + u'\u20B9')
