import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = store.Store(product_list)

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
            print("\n--- All active products ---")
            active_products = store_object.get_all_products()
            if not active_products:
                print("No products currently available")
            else:
                for product in active_products:
                    print(product.show())
            print("----------")

        elif user_choice == "2":
            total = store_object.get_total_quantity()
            print(f"We have {total} products in store\n")

        elif user_choice == "3":
            pass
        elif user_choice == "4":
            break
        else:
            print(f"Invalid choice '{user_choice}'. Please enter a number from 1 to 4")

