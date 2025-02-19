class Product:
    def __init__(self, name, price, quantity):
        """
        Initializes a product with a name, price, and quantity.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """
        Displays product information.
        """
        return f"Product: {self.name}, Price: {self.price:.2f} USD, Quantity: {self.quantity}"

    def update_quantity(self, new_quantity):
        """
        Updates the product quantity.
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")
