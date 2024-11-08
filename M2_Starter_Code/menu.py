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

Order = []
print("Welcome to the variety food truck.") 

place_order = True
while place_order:
    print("From which menu would you like to order? ")

    # Display menu categories
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get customer's menu selection
    menu_category = input("Type menu number: ")

    if menu_category.isdigit():
        menu_selection = int(menu_category)
        if menu_selection in menu_items:
            item_name = menu_items[menu_selection]
            print(f"Items available in {item_name}:")
            item_options = menu[item_name]

            # Display items in selected category
            j = 1
            item_lookup = {}
            for sub_item, price in item_options.items():
             if isinstance(price, (int, float)):
                print(f"{j}: {sub_item} - ${price:.2f}")
                item_lookup[j] = sub_item
                j += 1

            # Select specific item
            item_number = input("Select the item number: ")
            if item_number.isdigit() and int(item_number) in item_lookup:
                selected_item = item_lookup[int(item_number)]
                item_price = item_options[selected_item]

                # Ask for quantity
                quantity = input(f"How many {selected_item}s would you like? (default is 1) ")
                if not quantity.isdigit():
                    quantity = 1
                else:
                    quantity = int(quantity)

                # Add to Order
                Order.append({"Item name": selected_item, "Price": item_price, "Quantity": quantity})
                print(f"Added {quantity} x {selected_item} to your order.")
            else:
                print("Invalid item number.")

        else:
            print("That menu selection is not valid.")
    else:
        print("You didn't select a number.")

    # Continue or stop ordering
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
    if keep_ordering == 'n':
        print("Thank you for your order!")
        place_order = False
    elif keep_ordering != 'y':
        print("Please type 'Y' or 'N'.")

# Display Order summary
print("\nThis is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")  

for item in Order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    print(f"{item_name.ljust(25)} | ${price:.2f} | {quantity}")

# Calculate total cost
total_cost = sum(item["Price"] * item["Quantity"] for item in Order)
print(f"\nTotal cost of your Order: ${total_cost:.2f}")
