#wap to check a number is prime or not

def is_prime(num):

    for i in range(2,num):

        if num % i == 0:

            print(f"{num} is not prime")

            break

    else:

        print(f"{num} is prime")    


is_prime(17)
