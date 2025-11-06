class Product:
    def __init__(self, name, price, quantity):

        """ Adding validation as required by the specifications """

        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0 or quantity < 0:
            raise ValueError("Product price and quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True # Default to True as per specifications

    def get_quantity(self):

        """ Getter function for quantity - Returns the quantity (int) """

        return self.quantity

    def set_quantity(self, quantity):

        """ Setter function for quantity. If quantity reaches 0, deactivates the product """

        """ This method must accept a 'quantity' argument """

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        """ Adding the deactivation logic here """

        if self.quantity == 0:
            self.deactivate() # Calling the deactivate method


    def is_active(self):

        """ Getter function for active Returns True if the product is active, otherwise False """

        return self.active

    def activate(self):

        """ Activates the product """

        self.active = True

    def deactivate(self):

        """ Deactivates the product """

        self.active = False

    def show(self):

        """ Returns a string that represents the product """

        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity_to_buy):

        """

        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        It raises an Exception in case of a problem,

        """

        # Problem 1 - Check if the product is active
        if not self.is_active():
            raise Exception("Sorry, this product is not active")

        # Problem 2 - Check for valid purchase quantity
        if self.quantity <= 0:
            raise ValueError("Quantity cannot be negative")

        # Problem 3 - Check if there is enough stock
        if self.quantity < quantity_to_buy:
            raise ValueError(f"Sorry, there is not enough stock. Only {self.quantity} available")

        # --- IF ALL CHECKS ARE OK ---

        # 1 - Calculates the new quantity
        new_quantity = self.quantity - quantity_to_buy

        # 2- Use our setter to update the new quantity
        # This will also deactivate the product if it hits 0

        self.set_quantity(new_quantity)

        # 3- Calculate and return the total price

        total_price = self.price * quantity_to_buy
        return total_price

