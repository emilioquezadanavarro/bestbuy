import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = store.Store(product_list)

# This is a new helper function for Option 3
def handle_make_order(store_object):
    """
    Asks the user what they want to buy and places an order.
    Matches the demo output

    """
    print("\n----------------------------")
    print("Welcome to Order Management")
    print("----------------------------")

    active_products = store_object.get_all_products() # Get all active products to show the user

    if not active_products:
        print("No active products available, cannot place an order")
        print("-------")
        return

    for i, product in enumerate(active_products, start=1): # Show the user the available products
        print(f"{i}. {product.show()}")

    print("-----------------------------")
    print("When you want to finish order, enter empty text.\n")

    # Creating the shopping list

    shopping_list = [] # # This will be our list of (product, quantity) tuples

    # Shopping cart loop:
    while True:
        try:
            user_choice_str = input("\nWhich product # do you want to buy? ")
            if user_choice_str == "":
                break # Exit the shopping cart loop

            # Convert and validate the user input
            user_choice_str = int(user_choice_str)
            product_index = user_choice_str - 1 # Get the right index of the product to choose
            if not (0 <= product_index < len(active_products)):
                print("Invalid product number. Please try again\n")
                continue # restart the loop

            # If user choice is valid:
            chosen_product = active_products[product_index]
            quantity_user_choice_str = input("\nWhat amount do you want?: ")

            if quantity_user_choice_str == "":
                print("Cancelled item. Returning to product list.\n")
                continue # Restart the loop

            quantity_user_choice_num = int(quantity_user_choice_str)

            if quantity_user_choice_num < 0:
                print("Quantity must be greater than 0. Please, try again.\n")
                continue

            # Add to cart
            shopping_list.append((chosen_product, quantity_user_choice_num))
            print("Product added to list!\n")

        except ValueError:
            print("Invalid input. Please try again.\n")

    #Check if the cart is empty after the loop
    if not shopping_list:
        print("No items in cart, returning to main menu.\n")
        return

    # If cart is not empty
    print("\nPlacing your order...")
    try:
        # Calling the .order() method from Store class
        total_price = store_object.order(shopping_list)
        print("\nOrder Successful!")
        print(f"Total Price: {total_price:,.2f}\n")
        print("------------------------------")
    except Exception as e:
        # Catches errors like "Not enough stock" from product.buy()
        print(f"\n--- Order Failed! ---")
        print(f"Error: {e}")
        print("Please try again.\n")







def start(store_object):
    while True:

        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print("-----------")

        user_choice = input("Please, choose a number: ").strip()

        if user_choice == "1":
            print("\n--- All products available ---")
            active_products = store_object.get_all_products()
            if not active_products:
                print("No products currently available")
            else:
                for product in active_products:
                    print(product.show())
            print("----------")

        elif user_choice == "2":
            total = store_object.get_total_quantity()
            print(f"\nWe have {total} products in our store\n")

        elif user_choice == "3":
            handle_make_order(store_object)

        elif user_choice == "4":
            break

        else:
            print(f"Invalid choice '{user_choice}'. Please enter a number from 1 to 4")

start(best_buy)