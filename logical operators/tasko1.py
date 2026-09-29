# wap to check the given number is divisibe 3 and 5
# check the number is either divisible by 3 or 5
# else print "not divisibe by both"

number = int(input("enter the number: "))

if number % 3 == 0 and number % 5 == 0:

    print(f"the {number} is divisible by 3 and 5")

elif number % 3 == 0 or number % 5 == 0:

    print(f" the {number} is either by 3 or divisible by 5")

else:

    print("not divisible by 3 and 5")        