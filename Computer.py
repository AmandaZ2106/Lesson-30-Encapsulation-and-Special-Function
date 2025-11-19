class Computer:
    def __init__(self):
       self.__maxprice=990
    def sell(self):
        print("Selling for:",self.__maxprice)
    def price(self,price):
        self.__maxprice=price
        print("Price:",price)
com=Computer()
com.__maxprice=100
com.sell()
com.price(2000)
com.sell()