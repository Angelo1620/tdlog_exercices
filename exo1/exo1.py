"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""


class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
                
        
# Test the class

i = Item(10, 20)
print(i.price)  # Output: 10
print(i.weight)  # Output: 20

# Example of the class

i2 = Item(20, 30)
print(i2.price)  # Output: 20
print(i2.weight)  # Output: 30

# Testing  the price and weight attributes

i3 = Item(30, 40)
i3.price = 50
i3.weight = 60
print(i3.price)  # Output: 50
print(i3.weight)  # Output: 60