
#prime number 
# a whole number greater than 1 that can only be divided even;y by 1 and itseelf


number = 1

if number >1:

    for i in range(2 , number):

        if number % i == 0:

            print(f"{number} is not prime")

            break
    else:

        print(f"{number} is prime")


else:

    print("please enter a number above one")