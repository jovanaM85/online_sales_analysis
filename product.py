class Product:
    def __init__(self,name,price,quality):
        self.m_name = name
        self.m_price = price
        self.m_quality = quality
    def print_info(self):
        print("Name:",self.m_name,"Price:",self.m_price,"Quality:",self.m_quality)
    def add_quality(self,quality):
        self.m_quality += quality
        