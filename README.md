#  Online Sales Analysis  
 A Python project for managing products, shopping cart, and inventory.

## 📂 Project Structure  
 `online_sales_analysis/`  
- 📄 `product.py` – Defines the `Product` class  
- 📄 `product_manager.py` – Manages products (`ProductManager`)  
- 📄 `cart.py` – Implements the `Cart` class for the shopping cart  
- 📄 `main.py` – Main program logic  
- 📄 `.gitignore` – Ignores sensitive files and screenshots  
- 📄 `README.md` – Project documentation  

## 🛠 Features  
### **1️ Class `Product`**  
- `name` – Product name  
- `price` – Product price  
- `quantity` – Available quantity  
- `display_info()` – Displays product details  

### **2️ Class `ProductManager`**  
- `add_product(product)` – Adds a product to the inventory  
- `display_products()` – Displays all available products  
- `total_inventory_value()` – Calculates the total inventory value  
- `remove_product(product_name)` – Removes a product by name  

### **3️ Class `Cart`**  
- `add_to_cart(product)` – Adds a product to the cart  
- `display_cart()` – Displays the cart contents  
- `cart_total_value()` – Calculates the total cart value  

##  Usage  
1. **Run the program:**  
   ```sh
   python main.py  

