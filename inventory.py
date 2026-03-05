# Arturo Juarez Jr
# Final Project: inventory class
# June 27, 2025
# This is the Inventory class which stores the attributes
# for the inventory

class InventoryClass:
    # start with the __init__
    # this time we call more than just self
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price

    # now the gets 
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_stock(self):
        return self.__stock

    def get_price(self):
        return self.__price

    # to determine if there is sufficient stock or if its a return
    def purchase(self, purch_qty):
        # return (negative), add to stock
        if purch_qty < 0:
            self.__stock -= purch_qty  # subtracting a negative = adding
            return True
    # otherwise, make sure there's enough to purchase
        elif purch_qty <= self.__stock:
            self.__stock -= purch_qty
            return True
        else:
            return False


    def __str__(self):
        return f"{self.__id:<6} {self.__name:<25} ${self.__price:<8.2f} {self.__stock}"
