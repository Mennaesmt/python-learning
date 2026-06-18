#variables in python
x=5
y="menna"
z=5.0
w=True
print(type(x))
print(type(y))
print(type(z))
print(type(w))




#area calculator
length=int(input("enter the length of the rectangle: "))
width=int(input("enter the width of the rectangle: "))
area=length*width
print(f"The area of the rectangle is: {area}")


#shopping cart
items=input("enter the items you want to buy, separated by commas: ")
prices=input("enter the prices of the items, separated by commas: ")
items_list=items.split(",")
prices_list=prices.split(",")
total=0
for price in prices_list:
    total+=int(price)
print(f"The total cost of the items is: {total}")




#built-in functions
x=5.67
print(round(x))
print(abs(-5))
print(max(5, 10, 3))
print(min(5, 10, 3))
print(len("Hello"))
print(pow(2, 3))


import math
print(math.sqrt(16))
print(math.pi)      
print(math.e)
print(math.ceil(4.2))#rounds up to the nearest integer
print(math.floor(4.7))#rounds down to the nearest integer


#exercise1.1
import math
radius=float(input("enter the radius of the circle: "))
area=math.pi*math.pow(radius,2)
print(f"The area of the circle is: {area}")
