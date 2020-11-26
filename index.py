from user import User

restaurant = User()


while True:
    print("""
    Type Following Commands:

    ****************** For Restaurants ********************
    "RE" -> restaurant registration
    "AD" -> add dishes to particular restaurant
    "DD" -> delete dish of particular restaurant
    "UP" -> update price of particular restaurant
    "PT" -> update process time of particular restaurant
    "PM" -> print menu of particular restaurant

    ******************** For Users ************************
    "OR" -> order from particular restaurant
    "OD" -> order dish directly

    ******************** For Admin ************************
    "PO" -> print all orders
    "OO" -> print one order details

    ********************** Exit ***************************
    "EX" -> to Exit
    """)

    user_input = input().upper()

    if user_input == "RE":
        try:
            restaurants_num = abs(int(
                input("How many restaurants you have to register: ")))
            restaurant.register_restaurants(restaurants_num)
        except ValueError:
            print(
                "Error: Input value should be an integer")

    elif user_input == "AD":
        # Add Dishes
        restaurant_name = input(
            "Please provide restaurant name to add dishes: ").lower()

        if restaurant_name == "" or restaurant_name == "none"\
                or restaurant_name == "null":
            restaurant_name = input(
                "Invalid restaurant name.. please type again: ").lower()

        if restaurant_name in restaurant.restaurants:
            try:
                no_of_dishes = abs(int(
                    input("How many dishes you have to add" +
                          f" in {restaurant_name} restaurant: ")))
                restaurant.add_items_to_menu(restaurant_name, no_of_dishes)
            except ValueError:
                print(
                    "Error: Input value should be an integer")
        else:
            print(
                "Error: Invalid input.. restaurant data does not exist!!")

    elif user_input == "DD":
        # Delete Dish
        restaurant_name = input(
            "To remove dish from menu.." +
            " please provide restaurant name: ").lower()

        if restaurant_name == "" or restaurant_name == "none"\
                or restaurant_name == "null":
            restaurant_name = input(
                "Invalid restaurant name.. please type again: ").lower()

        if restaurant_name in restaurant.restaurants:

            restaurant.remove_items_from_menu(
                restaurant_name)
        else:
            print(
                "Error: Invalid input.. restaurant data does not exist!!")

    elif user_input == "UP":
        # Update Price
        restaurant_name = input(
            "To update price in menu.." +
            " please provide restaurant name: ").lower()

        if restaurant_name == "" or restaurant_name == "none"\
                or restaurant_name == "null":
            restaurant_name = input(
                "Invalid restaurant name.. please type again: ").lower()

        if restaurant_name in restaurant.restaurants:
            selected_restaurant_menu = restaurant.\
                restaurants[restaurant_name]["menu"]

            dish_name = input("In which dish you have to edit price: ").lower()

            if dish_name == "" or dish_name == "none" or dish_name == "null":
                dish_name = input(
                    "Invalid dish name.. please type again: ").lower()

            dish_found = False

            for i in range(len(selected_restaurant_menu)):
                if selected_restaurant_menu[i]["dish_name"] == dish_name:
                    updated_price = abs(int(input(
                        f"Provide new price of {dish_name}: ")))

                    restaurant.update_price(
                        restaurant_name, dish_name, updated_price)

                    dish_found = True

            if not(dish_found):
                print("Error: Invalid input.. dish name does not exist!!")
        else:
            print(
                "Error: Invalid input.. restaurant data does not exist!!")

    elif user_input == "PT":
        # Update Process Time
        restaurant_name = input(
            "To update process time in menu.. " +
            "please provide restaurant name: ").lower()

        if restaurant_name == "" or restaurant_name == "none"\
                or restaurant_name == "null":
            restaurant_name = input(
                "Invalid restaurant name.. please type again: ").lower()

        if restaurant_name in restaurant.restaurants:
            selected_restaurant_menu = restaurant.\
                restaurants[restaurant_name]["menu"]

            dish_name = input(
                "In which dish you have to update process time: ").lower()

            if dish_name == "" or dish_name == "none" or dish_name == "null":
                dish_name = input(
                    "Invalid dish name.. please type again: ").lower()

            dish_found = False

            for i in range(len(selected_restaurant_menu)):
                if selected_restaurant_menu[i]["dish_name"] == dish_name:
                    updated_process_time = abs(int(input(
                        f"Provide new process time of {dish_name}: ")))

                    restaurant.update_process_time(
                        restaurant_name, dish_name, updated_process_time)

                    dish_found = True

            if not(dish_found):
                print("Error: Invalid input.. dish name does not exist!!")

        else:
            print(
                "Error: Invalid input.. restaurant data does not exist!!")

    elif user_input == "PM":
        # Print Menu
        restaurant_name = input("Get menu of particuler restaurant: ").lower()

        if restaurant_name == "" or restaurant_name == "none"\
                or restaurant_name == "null":
            restaurant_name = input(
                "Invalid restaurant name.. please type again: ").lower()

        restaurant.print_menu(restaurant_name)

    elif user_input == "OR":
        # Order from restaurant
        restaurant_name = input(
            "Type restaurant name.. to Get menu " +
            "of particuler restaurant: ").lower()

        if restaurant_name == "" or restaurant_name == "none"\
                or restaurant_name == "null":
            restaurant_name = input(
                "Invalid restaurant name.. please type again: ").lower()

        if restaurant_name in restaurant.restaurants:
            restaurant.print_menu(restaurant_name)

            try:
                no_of_dishes = abs(
                    int(input("How many dishes you have to order: ")))

                if no_of_dishes > 3:
                    print("Restaurant can take three orders at a time..")
                else:
                    restaurant.order_by_restaurant(
                        restaurant_name, no_of_dishes)
            except ValueError:
                print(
                    "Error: Input value should be an integer")
        else:
            print(
                "Error: Oops something went wrong.. " +
                "restaurant data does not exist!!")

    elif user_input == "OD":
        # Order Dish
        try:
            no_of_dishes = abs(
                int(input("How many dishes you want to order: ")))

            if no_of_dishes > 3:
                print("Restaurant can take three orders at a time..")
            else:
                restaurant.order_dish(no_of_dishes)

        except ValueError:
            print(
                "Error: Input value should be an integer")

    elif user_input == "PO":
        restaurant.all_order_details()

    elif user_input == "OO":
        try:
            order_no = abs(int(
                input("Type order number to get " +
                      "details of particular order: ")))
            restaurant.one_order_detail(order_no)
        except ValueError:
            print(
                "Error: Input value should be an integer")

    elif user_input == "EX":
        break
