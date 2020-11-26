class Restaurant():
    def __init__(self):
        self.restaurants = {}
        self.processing_limit = 3

    def register_restaurants(self, restaurants_num):
        for i in range(restaurants_num):
            restaurant_details = {}

            restaurant_name = input(f"Type restaurant {i + 1} name: ").lower()
            if restaurant_name == "" or restaurant_name == "none" \
                    or restaurant_name == "null":
                restaurant_name = input(
                    "Invalid restaurant name.. please type again: ").lower()
                if restaurant_name == "" or restaurant_name == "none" or \
                        restaurant_name == "null":
                    break
            restaurant_details["name"] = restaurant_name
            restaurant_details["processing_limit"] = self.processing_limit
            restaurant_details["order_history"] = []
            self.restaurants[restaurant_name] = restaurant_details

        print(self.restaurants)
