from product import Product
from product_manager import ProductManager
from cart import Cart
import random

# Create an instance of ProductManager
manager = ProductManager()

# Add some products (Modified names & quantities)
manager.add_product(Product("Gaming Laptop", 1500, 3))
manager.add_product(Product("Smartphone", 900, 12))
manager.add_product(Product("Wireless Headphones", 180, 15))
manager.add_product(Product("4K Monitor", 400, 5))
manager.add_product(Product("Gaming Mouse", 60, 10))

# Create an instance of Cart
cart = Cart()

# Select 3 random products from the available ones
random_products = random.sample(manager.products, 3)
for product in random_products:
    cart.add_to_cart(product)

# Display cart contents
cart.display_cart()
