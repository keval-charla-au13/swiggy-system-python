from food_items import Food
import time


class User(Food):
    def __init__(self):
        super().__init__()
        self.order_number = 1
        self.all_orders = {}

    def order_by_restaurant(self, restaurant_name, no_of_dishes):
        dish_in_process = {}

        # if len(dish_in_process) <= 3:
        for i in range(no_of_dishes):
            dish_name = input(
                f"order number {i + 1} from {restaurant_name}: ").lower()

            if dish_name == "" or dish_name == "none" or dish_name == "null":
                dish_name = input(
                    "Invalid dish name.. please type again: ").lower()

            if dish_name in self.all_dishes:
                selected_restaurant_menu = self.\
                    restaurants[restaurant_name]["menu"]

                # print(selected_restaurant_menu)
                for i in range(len(selected_restaurant_menu)):
                    dishes = {}
                    # print(selected_restaurant_menu[i]["dish_name"])

                    if dish_name == selected_restaurant_menu[i]["dish_name"]:
                        dishes["dish_name"] = dish_name
                        processing_time = \
                            selected_restaurant_menu[i]["process_time"]
                        dishes["process_time"] = processing_time

                        # print(len(dish_in_process))

                        if len(dish_in_process) < 3:
                            dish_in_process[dish_name] = dishes
                            print(
                                "******************** Your order has been " +
                                "successfully placed... ********************")

                            order = {}
                            order["order_number"] = self.order_number
                            order["dish_name"] = dish_name
                            order["price"] = \
                                selected_restaurant_menu[i]["price"]
                            order["restaurant_name"] = restaurant_name

                            if restaurant_name in self.all_orders:
                                self.all_orders[self.order_number] = order
                            else:
                                self.all_orders[self.order_number] = {}
                                self.all_orders[self.order_number] = order

                            self.restaurants[restaurant_name]["order_history"].append(
                                order)
                            self.order_number += 1
                        else:
                            print(
                                "Maximum processing limit " +
                                "reach... you have to wait some more time")
            else:
                print(f"{restaurant_name} don't have this dish!!")
                break

        # print("All orders of restaurants: ", self.all_orders)
        # print(self.restaurants)
        # print("Maximum processing", dish_in_process)
        if dish_name in self.all_dishes:
            count = 1
            for i in dish_in_process:
                processing_time = dish_in_process[i]["process_time"]
                # dish = dish_in_process[i]["dish_name"]

                while processing_time > -1:
                    m, s = divmod(processing_time, 60)
                    h, m = divmod(m, 60)
                    time_left = str(h).zfill(2) + ":" + \
                        str(m).zfill(2) + ":" + str(s).zfill(2)
                    print(
                        time_left + "\r" +
                        f"Your order {count} is getting ready... ", end="")
                    time.sleep(1)
                    processing_time -= 1

                count += 1

                total_waiting_time = 10

            while total_waiting_time > -1:
                m, s = divmod(total_waiting_time, 60)
                h, m = divmod(m, 60)
                time_left = str(h).zfill(2) + ":" + \
                    str(m).zfill(2) + ":" + str(s).zfill(2)
                print(
                    time_left + "\r" +
                    "Your order will reach you soon in approx... ", end="")
                time.sleep(1)
                total_waiting_time -= 1

            dish_in_process = {}
            print("Your order successfully delivered... " +
                  "Thank You for Shopping!!")

    def order_dish(self, no_of_dishes):
        total_orders = []
        temp = {}
        count = 1
        dish_in_process = {}

        for i in range(no_of_dishes):
            dish_name = input(f"order number {i + 1}: ").lower()

            if dish_name == "" or dish_name == "none" or dish_name == "null":
                dish_name = input(
                    "Invalid dish name.. please type again: ").lower()

            if dish_name in self.all_dishes:
                total_orders.append(dish_name)
            else:
                print(f"We did not find {dish_name} dish with our partners..")
                break

        if dish_name in self.all_dishes:
            for order in total_orders:
                if order in self.all_dishes:
                    for i in range(len(self.all_dishes[order])):
                        restaurant_name = self.\
                            all_dishes[order][i]["restaurant_name"]
                        price = self.all_dishes[order][i]["price"]

                        if restaurant_name not in temp:
                            temp[restaurant_name] = f"{price},{count}"
                        else:
                            old_price, count = temp[restaurant_name].split(",")
                            next_price = int(old_price) + price
                            count = int(count)
                            count += 1
                            temp[restaurant_name] = f"{next_price},{count}"

            # print(temp)

            restaurant_with_dishes = {}

            for key, value in temp.items():
                price, count = value.split(",")

                if int(count) == len(total_orders):
                    restaurant_with_dishes[key] = int(price)

            # print(restaurant_with_dishes)

            restaurant_with_min_price = sorted(
                restaurant_with_dishes,
                key=lambda min_price: restaurant_with_dishes[min_price])

            # print(restaurant_with_min_price)

            restaurant_name = restaurant_with_min_price[0]
            selected_restaurant_menu = self.\
                restaurants[restaurant_name]["menu"]

            for i in range(len(selected_restaurant_menu)):
                dishes = {}

                for dish_name in total_orders:
                    if dish_name == selected_restaurant_menu[i]["dish_name"]:
                        dishes["dish_name"] = dish_name
                        processing_time = \
                            selected_restaurant_menu[i]["process_time"]
                        dishes["process_time"] = processing_time

                        if len(dish_in_process) < 3:
                            dish_in_process[dish_name] = dishes

                            order = {}
                            order["order_number"] = self.order_number
                            order["dish_name"] = dish_name
                            order["price"] = \
                                selected_restaurant_menu[i]["price"]
                            order["restaurant_name"] = restaurant_name

                            if restaurant_name in self.all_orders:
                                self.all_orders[self.order_number] = order
                            else:
                                self.all_orders[self.order_number] = {}
                                self.all_orders[self.order_number] = order

                            self.restaurants[restaurant_name]["order_history"].append(
                                order)
                            self.order_number += 1

            # print("All orders of restaurants: ", self.all_orders)

            # print("Restaurant data: ", self.restaurants)
            count = 1

            for i in dish_in_process:
                processing_time = dish_in_process[i]["process_time"]
                # dish = dish_in_process[i]["dish_name"]

                while processing_time > -1:
                    m, s = divmod(processing_time, 60)
                    h, m = divmod(m, 60)
                    time_left = str(h).zfill(2) + ":" + \
                        str(m).zfill(2) + ":" + str(s).zfill(2)
                    print(
                        time_left + "\r" +
                        f"Your order {count} is getting ready... ", end="")
                    time.sleep(1)
                    processing_time -= 1

                count += 1

                total_waiting_time = 10

            while total_waiting_time > -1:
                m, s = divmod(total_waiting_time, 60)
                h, m = divmod(m, 60)
                time_left = str(h).zfill(2) + ":" + \
                    str(m).zfill(2) + ":" + str(s).zfill(2)
                print(
                    time_left + "\r" +
                    "Your order will reach you soon in approx... ", end="")
                time.sleep(1)
                total_waiting_time -= 1

            dish_in_process = {}

            print("Your order successfully delivered... " +
                  "Thank You for Shopping!!")

    def all_order_details(self):
        for value in self.all_orders.values():
            print(value)

    def one_order_detail(self, order_no):
        for key, value in self.all_orders.items():
            if order_no == key:
                print(value)
