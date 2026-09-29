# define a function to check the given number is perfect or not

def is_perfect(num):

    sum = 0

    for i in range(1, num):


        if num % i == 0:

            sum += i

    print(f"perfect" if sum == num else "not perfect")   


is_perfect(6)        

