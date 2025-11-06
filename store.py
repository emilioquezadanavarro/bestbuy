from products import Product

class Store:

    def __init__(self,initial_product_list = None): # Accepts also an optional argument
        """
        Initializes a new store.
        If a list of products is provided, the store is initialized with that list.
        Otherwise, start with an empty list.
        """

        if initial_product_list is None:
            # If no list is provided, create a new, empty list
            # and store the products in the instance variable "self.list_of_products"

            self.list_of_products = []

        else:
            # If a list was provided, store that list in the instance variable "self.list_of_products"
            self.list_of_products = initial_product_list

    def add_product(self,product_to_add):

        """ Adds a single Product object to the store's list """

        # Check if it is a Product
        if not isinstance(product_to_add, Product):
            raise TypeError(f"You can only add Products objects, not {type(product_to_add)}")

        # Access the instance list called "list_of_products" only if the "if" statement is False
        # and append the new product
        self.list_of_products.append(product_to_add)

        # Print a message to the user.
        print(f"Added {product_to_add.name}")

    def remove_product(self,product_to_remove):

        """ Removes a single Product object from the store's list """

        # Check if it is a Product
        if not isinstance(product_to_remove, Product):
            raise TypeError(f"You can only remove Products objects, not {type(product_to_remove)}")

        # Existence check
        # Checks if the OBJECT is in the list.
        if product_to_remove in self.list_of_products:
            # If it exists, it removes the object and prints a message to the user.
            self.list_of_products.remove(product_to_remove)
            print(f"{product_to_remove.name} was removed")
        else:
            # If it doesn't exist,a raise an error
            raise Exception(f"Product {product_to_remove.name} does not exist")








