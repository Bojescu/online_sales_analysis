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
    
    def remove_product(self, product_name):
        """
        Removes a product from the inventory by name.
        """
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print(f"Product '{product_name}' removed from inventory.")
                return
            print(f"Product '{product_name}' not found in inventory.")
