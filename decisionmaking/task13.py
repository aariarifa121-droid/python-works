#Divisible by 5 or 10: Check whether a number is divisible by 5 or 10.

number = int(input("enter the number"))

if number % 5 == 0 and number % 10 == 0:

    print(f"{number} is divisible ")

else:

    print(f"{number} is not divisible")
    
