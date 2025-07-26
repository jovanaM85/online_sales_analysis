from product import Product
class ProductManager:
    def __init__(self):
        self.m_list = []
    def add_product(self,product):
        self.m_list.append(product)
    def print_products(self):
        for product in self.m_list:
            product.print_info()
    def calculate_quality(self):
        count_price = 0
        for product in self.m_list:
            count_price = count_price + product.m_quality* product.m_price
        print(count_price)    