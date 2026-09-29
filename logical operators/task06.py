

#if n is odd print wired
# if n even and in the inclusive range of 2 to 5 print not wired 
# if n is even and in the inclusive rangr 6 to 20 print wired
# if n is even and geater than 20 print wired

number = int(input("enter the number: "))

if number % 2 != 0:

    print("wired")

elif number % 2 == 0 and number >= 2 and number <= 5:

    print("not wired")

elif number % 2 == 0 and number >= 6 and number <= 20:

    print("wired")

elif number % 2 == 0 and number > 20:

    print("not wired")

else:

    print("thank you")
