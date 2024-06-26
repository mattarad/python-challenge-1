# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input(f"Enter the Item Number you would like to purchase: (1 - {i - 1}) ")


            # 3. Check if the customer typed a number
            if menu_selection.isdigit():

                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():

                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input("How many would you like to purchase? ")

                    # Check if the quantity is a number, default to 1 if not
                    quantity = 1 if not quantity.isdigit() else int(quantity)

                    # Add the item name, price, and quantity to the order list
                    # get list of keys in each item dictionary in the order
                    order_keys = [item_dict.get("Item name") for item_dict in order if "Item name" in item_dict]

                    if item_name in order_keys:
                        # if item_name is in order_keys, we pull the index of the item to add to the quantity
                        index = next((i for i, order_dict in enumerate(order) if order_dict.get("Item name") == item_name), None)
                        order[index]["Quantity"] += quantity
                    else: # if item hasn't been added, it appends item to customer_order
                        order.append({
                                "Item name": item_name,
                                "Price": menu_items[menu_selection]["Price"],
                                "Quantity": quantity
                            })
            # Tell the customer that their input isn't valid
            else:
                print("Invalid input")
                print(f"you must enter a number between  (1 - {i - 1})")

                # Tell the customer they didn't select a menu option
                print(":(")
                print("You did not select a valid item number.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        # 5. Check the customer's input
        match keep_ordering:

                # Keep ordering
                case 'y':
                # Exit the keep ordering question loop
                    break

                # Complete the order
                case 'n':
                # Since the customer decided to stop ordering, thank them for
                # their order
                    print("Thank you for ordering with us!")                    

                # Exit the keep ordering question loop
                    place_order = False
                    break

                case _:
                    # Tell the customer to try again
                    print("invalid entry, please try again.")


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

split_one = "--------------------------"
split_two = "--------"
split_three = "----------"

print("Item name                 | Price  | Quantity")
print(f"{split_one}|{split_two}|{split_three}")

split_one_len = len(split_one)
split_two_len = len(split_two) - 1 # minus one to account for dollar sign ($)
split_three_len = len(split_three)

# 6. Loop through the items in the customer's order
for item in order:
    # print(item)
    if type(item) is dict:
        # 7. Store the dictionary items as variables
        current_item = item["Item name"]
        current_price = item["Price"]
        current_quantity = item["Quantity"]

        # 8. Calculate the number of spaces for formatted printing
        spacing_one_len = split_one_len - len(current_item)
        spacing_two_len = split_two_len - (len(str(current_price)) +1) # minus 1 to account for dollar
        spacing_three_len = split_three_len - (len(str(current_quantity)))

        # 9. Create space strings
        space_one = spacing_one_len * " "
        space_two = spacing_two_len * " "
        space_three = int(spacing_three_len/2) * " "


        # 10. Print the item name, price, and quantity
        print(f"{current_item}{space_one}| ${current_price}{space_two}|{space_three}{current_quantity}")


# 11. Calculate the cost of the order using list comprehension
print("-" * 50)
prices = [round(item['Price'] * item['Quantity'], 2) for item in order]

# and print the prices.
print(prices)
print(f"Order Total: {sum(prices):,.2f}")
