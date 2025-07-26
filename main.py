from product_manager import ProductManager
from product import Product
from cart import Cart

pm = ProductManager()
pm.add_product(Product("Tastatura",10,15))
pm.add_product(Product("Mis",5,55))
pm.add_product(Product("Monitor",100,70))
pm.print_products()
pm.calculate_quality()
pm.remove_product("Monitor")
pm.print_products()
cart = Cart()
cart.add_product(Product("Mis",5,1))
cart.add_product(Product("Monitor",10,1))
cart.add_product(Product("Tastatura",100,1))
cart.print_products()
cart.calculate_price()