#wap to check the given number divisblee by 3 and 5

number  = int(input("enter the number: "))

if number % 3 == 0:

    if number % 5 == 0:

        print("divisible by 3 and 5")

    else:

        print(f"{number} divisble by 3 but not by 5")

else:

    print(f"{number} not divisble by 3")            