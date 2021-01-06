# include library

from OOP import Shirt
from OOP import SalesPerson


# Code start here !

Shirt_One = Shirt('blue' , 'S' , 'short sleeve' , 15)
salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
print(Shirt_One.colour)
print(Shirt_One.price)
Shirt_One.change_price(10)
print(Shirt_One.price)

print(Shirt_One.discount(0.2))