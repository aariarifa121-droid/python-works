# wap to print all the even factors of the given number

number = 10

for i in range(1, number + 1):

    if number % i == 0 and i % 2 == 0:

        print(i)

