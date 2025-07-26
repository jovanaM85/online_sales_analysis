from product_manager import ProductManager
from product import Product
from cart import Cart

pm = ProductManager()
pm.add_product(Product("Tastatura",10,3))
pm.add_product(Product("Mis",10,55))
pm.add_product(Product("Monitor",100,22))
cart = Cart()
cart.add_product(Product("Mis",5,1))
cart.add_product(Product("Monitor",10,1))
cart.add_product(Product("Tastatura",100,1))
cart.print_products()
cart.calculate_price()

