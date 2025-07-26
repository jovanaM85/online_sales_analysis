from product_manager import ProductManager
from product import Product

pm = ProductManager()
pm.add_product(Product("Tastatura",10,15))
pm.add_product(Product("Mis",5,55))
pm.add_product(Product("Monitor",100,70))
pm.print_products()
pm.calculate_quality()
pm.remove_product("Monitor")
pm.print_products()