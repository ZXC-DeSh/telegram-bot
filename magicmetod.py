class Item:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self,other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other,int):
            return self.price + other    
    
    def __sub__(self,other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other,int):
            return self.price - other
        
    def __mul__(self,other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other,int):
            return self.price * other
        
    def __truediv__(self,other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other,int):
            return self.price / other

item_1 = Item('Видюха',41244,1)
item_2 = Item('Проц',124534,0.34)

total_price = item_1 + 1000
total_price1 = item_1 - 1000
total_price2 = item_1 * 1000
total_price3 = item_1 / 1000
print(total_price,total_price1,total_price2,total_price3)