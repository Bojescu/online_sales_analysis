from product import Product

class Cart:
    def __init__(self):
        """
        Initializes an empty cart.
        """
        self.cart_items = []

    def add_to_cart(self, product):
        """
        Adds a product to the cart.
        """
        self.cart_items.append(product)
        print(f"Added '{product.name}' to the cart.")

    def total_cart_value(self):
        """
        Calculates the total value of all items in the cart.
        """
        return sum(product.price * product.quantity for product in self.cart_items)

    def display_cart(self):
        """
        Displays all products in the cart.
        """
        if not self.cart_items:
            print("The cart is empty.")
        else:
            print("\nCart Items:")
            for product in self.cart_items:
                print(product.display_info())

            print(f"\nTotal Cart Value: {self.total_cart_value():.2f} USD")
