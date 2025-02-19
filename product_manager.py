from product import Product

class ProductManager:
    def __init__(self):
        """
        Initializes a product manager with an empty list of products.
        """
        self.products = []

    def add_product(self, product):
        """
        Adds a new product to the inventory.
        """
        self.products.append(product)

    def display_products(self):
        """
        Displays all products in the inventory.
        """
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        """
        Returns the total value of all products in stock.
        """
        return sum(product.price * product.quantity for product in self.products)
