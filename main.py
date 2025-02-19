from product import Product
from product_manager import ProductManager

# Create an instance of ProductManager
manager = ProductManager()

# Add some products
manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Phone", 800, 10))
manager.add_product(Product("Headphones", 150, 20))

# Display all products
print("\nAvailable Products:")
manager.display_products()

# Display total inventory value
print(f"\nTotal Inventory Value: {manager.total_inventory_value():.2f} USD")
