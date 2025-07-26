from product import Product
class Cart:
    def __init__(self):
        self.cart_items  = []

    def add_product(self,product):
        self.cart_items.append(product)
    def print_products(self):
        for product in self.cart_items:
            product.print_info()
    def calculate_price(self):
        count_price = 0
        for product in self.cart_items:
            count_price = count_price + product.m_quality* product.m_price
        print(count_price)    