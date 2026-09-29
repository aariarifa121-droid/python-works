
# ask the user enter the number if it is under 10
#display the message "too low" if the number is between 10 and 20 display correctly otherwise display "too high"

number = int(input("enter the number: "))

if number < 10:

    print("too low")

elif number >= 10 and number <= 20:

    print("correctly")

else:

    print("too high")    