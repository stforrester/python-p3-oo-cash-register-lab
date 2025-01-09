#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0, total=0, items=None, last_transaction=0):
        self.discount = discount
        self.total = total
        self.items = items
        self.items = items if items is not None else []
        self.last_transaction = last_transaction
    
    def add_item(self, title, price, quantity=1):
        self.total += price*quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price*quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total - (self.total * self.discount * .01))
            print(f"After the discount, the total comes to ${self.total}.")
        if self.discount == 0:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        self.total = self.total - self.last_transaction