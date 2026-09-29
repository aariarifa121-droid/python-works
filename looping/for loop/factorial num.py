#wap to get the factorial of numbers from 2 to 6

for num in range(2,7):

    product = 1

    for i in range(1 , num+ 1):

        product *= i

    print(f"the factorial of {num} is {product}") 