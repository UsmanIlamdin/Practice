
'''


Object-Oriented Programming (OOP) Vocabulary

'''


'''
Object has characteristic and do some action
these characteristic  are attributes and actions
are methods in OOP

'''

'''

class - a blueprint consisting of methods and attributes
object - an instance of a class. It can help to think of 
objects as something in the real world like a yellow pencil, 
a small dog, a blue shirt, etc. However, as you'll see later 
in the lesson, objects can be more abstract.

attribute - a descriptor or characteristic. Examples 
would be color, length, size, etc. These attributes can 
take on specific values like blue, 3 inches, large, etc.
method - an action that a class or object could take
OOP - a commonly used abbreviation for object-oriented programming
encapsulation - one of the fundamental ideas behind object-oriented 
programming is called encapsulation: you can combine functions and 
data all into a single entity. In object-oriented programming, this 
single entity is called a class. Encapsulation allows you to hide 
implementation details much like how the scikit-learn package hides 
the implementation of machine learning algorithms.

'''



class Shirt:
    def __init__(self , shirt_colour , shirt_size , shirt_style , shirt_price):
        self.colour = shirt_colour
        self.size   = shirt_size
        self.style  = shirt_style
        self.price  = shirt_price
    def change_price(self, new_price):
        """
        change price using stamp method
        """
        self.price = new_price
    
    def discount(self, discount):
        """
        return price after discount
        """
        return self.price*(1-discount)
class Pants:
    
    def __init__(self, paint_color, paint_waist_size, paint_length, paint_price):
        self.color=paint_color
        self.waist_size=paint_waist_size
        self.length=paint_length
        self.price=paint_price
    
    def change_price(self, new_price):
        
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)


# def check_results():
#     pants = Pants('red', 35, 36, 15.12)
#     assert pants.color == 'red'
#     assert pants.waist_size == 35
#     assert pants.length == 36
#     assert pants.price == 15.12
    
#     pants.change_price(10) == 10
#     assert pants.price == 10 
    
#     assert pants.discount(.1) == 9
    
#     print('You made it to the end of the check. Nice job!')

# check_results()


class SalesPerson:
    
    def __init__(self,first_name,last_name,employee_id,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0
        
    def sell_pants(self, pants_object):

        self.pants_sold.append(pants_object)

    def display_sales(self):
       


        for pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'\
                  .format(pants.color, pants.waist_size, pants.length, pants.price))
    
    def calculate_sales(self):
        ###The calculate_sales method sums the total price of all pants sold

        #Args: None

        #Returns:
        #   float: sum of the price for all pants sold
        
        ###

        total = 0
        for pants in self.pants_sold:
            total += pants.price
            
        self.total_sales = total
        
        return total
    
    def calculate_commission(self, percentage):
       

        sales_total = self.calculate_sales()
        return sales_total * percentage 

# def check_results():
#     pants_one = Pants('red', 35, 36, 15.12)
#     pants_two = Pants('blue', 40, 38, 24.12)
#     pants_three = Pants('tan', 28, 30, 8.12)
    
#     salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
#     assert salesperson.first_name == 'Amy'
#     assert salesperson.last_name == 'Gonzalez'
#     assert salesperson.employee_id == 2581923
#     assert salesperson.salary == 40000
#     assert salesperson.pants_sold == []
#     assert salesperson.total_sales == 0
    
#     salesperson.sell_pants(pants_one)
#     salesperson.pants_sold[0] == pants_one.color
    
#     salesperson.sell_pants(pants_two)
#     salesperson.sell_pants(pants_three)
    
#     assert len(salesperson.pants_sold) == 3
#     assert round(salesperson.calculate_sales(),2) == 47.36
#     assert round(salesperson.calculate_commission(.1),2) == 4.74

Shirt('red' , 'S' , 'short sleeve' , 15)

Shirt_One = Shirt('blue' , 'S' , 'short sleeve' , 15)


print(Shirt_One.price)
print(Shirt_One.colour)
print(Shirt_One.style)
print(Shirt_One.size)


Shirt_One.change_price(20)

print(Shirt_One.price)

Shirt_One.discount(0.2)

print(Shirt_One.discount(0.2))

Shirt_Two = Shirt('red' , 'L' , 'half sleeve' , 10)
 
Shirt_Three = Shirt('blue' , 'XL' , 'medium sleeve' , 12)

Shirt_Four = Shirt('orange' , 'XXL' , 'short sleeve' , 20)

total = [Shirt_One , Shirt_Two , Shirt_Three , Shirt_Four]

for shirt in range(len(total)):
    print(total[shirt].colour)