"""
Ask for the total price of the bill, then ask how 
many diners there are. Divide the total bill by the 
number of diners and show how much each 
person must pay.

"""

total_price = int(input("enter the total price:"))

people = int(input("total count:"))

amount = total_price / people

print(f"everyone should pay {amount}")