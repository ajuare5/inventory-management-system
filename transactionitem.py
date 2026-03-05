# Arturo Juarez Jr.
# Final Project: transactionitem class
# June 27, 2025
# This is the Transaction Item class which contains the attributes
# for the item that is being returned or bought

class TransactionItemClass:
    # define __init__
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__quantity = 0
        self.__price = 0.0
    # now the gets and sets for the attributes
    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_qty(self):
        return self.__quantity

    def set_qty(self, new_qty):
        self.__quantity = new_qty

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
        
    # method to calculate the cost (qty x price)
    def calc_cost(self):
        return self.__quantity * self.__price

    # override the __str__
    def __str__(self):
        total_cost = self.calc_cost()
        # we will use the <x to keep the printed column alligned and control space used
        return f"{self.__id:<6} {self.__name:<25} {self.__quantity:<5} ${self.__price:<8.2f} ${total_cost:<.2f}"
