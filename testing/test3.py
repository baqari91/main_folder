# li = ['Car (mixer,100,2)', 'Car (samsung,1000,3'), 'Car (samsung1,10001,3)', 'Car (a,1,2)']




# class Test:
#     default_dict = {}
#     def __init__(self,name,price,quantity):
#             self.name = name
#             self.price = price
#             self.quantity = quantity

#             if self.name not in Test.default_dict:
#                 Test.default_dict[self.name]= {price: self.price,quantity: self.quantity}
#     def remove_item(self, product_name):
#          if product_name in Test.default_dict:
#               del Test.default_dict[product_name]
class Cart:
    
    def __init__(self):
            self.cart_items = {}

    def add_item(self, product_name:str,price:float,quantity:int):
        if product_name in self.cart_items:
              print('Product already in cart. Updating quantity.')
              self.cart_items[product_name]['quantity'] += quantity
        else:
              self.cart_items[product_name] = {'price':price,'quantity':quantity}

    def remove_item(self, product_name):
        if product_name in self.cart_items:
            del self.cart_items[product_name]
            return (f'product: "{product_name}" deleted')
        else:
             return 'enter corecrtly item name'
            
    def show_product_list(self):
        products = ''
        numb = 1
        for i in self.cart_items:
             products += f'{numb}: {i} - Price: {self.cart_items[i]["price"]} - Quantity: {self.cart_items[i]["quantity"]} - Total: {self.cart_items[i]["price"]*self.cart_items[i]["quantity"]}\n'
             numb += 1
        return products
    
    def total_price(self):
        jami = 0
        for i in self.cart_items:
            jami += self.cart_items[i]['quantity'] * self.cart_items[i]['price']
        return "Total price: ",jami
            

cart = Cart()
cart.add_item('product1',30,3)
cart.add_item('product2',50,2)
cart.add_item('product3',20,6)
cart.add_item('product4',1,100)
cart.add_item('product4',1,100)
print(cart.cart_items)
print(cart.show_product_list())
print(cart.remove_item('product2'))
print(cart.show_product_list())
print(cart.total_price())










# Test.add_item('1','name',3,5)

# print(Test)
    
# while default_dict:
#     a = input("enter product name: ")
#     if a in default_dict:
#         del default_dict[a]
#         print(default_dict)