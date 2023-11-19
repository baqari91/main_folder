#დავალება 1 წრის კლასი
class Cyrcle:
    def __init__(self,radius):
        self.radius = radius

    def area (self):
        return 3.14159 * self.radius ** 2
    def perimetr(self):
        return 2 * 3.14159 * self.radius

my_cyrcle1 = Cyrcle(15)

print(my_cyrcle1.perimetr())
print(my_cyrcle1.area())


#დავალება 2 კალკულატორის კლასი 2
class Calc:
    def __init__(self,numb_1,numb_2):
        self.numb_1 = numb_1
        self.numb_2 = numb_2

    def addition(self):
        return self.numb_1 + self.numb_2
    def subtraction(self):
       return self.numb_1 - self.numb_2
    def multiplication(self):
       return self.numb_1 * self.numb_2
    def division(self):
       return self.numb_1 / self.numb_2
    
calc_1 = Calc(70,10)
print(calc_1.addition())
print(calc_1.subtraction())
print(calc_1.multiplication())
print(calc_1.division())



# დავალება 3 კალათის კლასი
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


# დავალება 3 საბანკო ანგარიშის კლასი
class Bank_acount:
    def __init__(self):
        self.bank_account = 0
    def add_money(self, number:float):
        self.bank_account += number
        return f'An addition of: {number} units of currency, resulting in a balance of : {self.bank_account}'
    def withdraw_cash(self, number:float):
        self.bank_account -= number
        return f'A withdrawal of: {number}.  units of currency, reducing the balance to: {self.bank_account}'
    def tranfers_money(self, number:float):
        self.bank_account -= number
        return f'A transfer of 50 units of currency: {number}. resulting in a remaining balance of {self.bank_account}'
bank_acount = Bank_acount()
print (bank_acount.add_money(200))
print (bank_acount.withdraw_cash(50))
print (bank_acount.tranfers_money(50))
 
