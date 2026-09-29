# wap to get the armstrong num from 1 to 1000


for num in range(1,1001):

    sum =0
    temp = num
    length = len(str(num))

    while(num > 0):

        digit = num % 10

        sum += digit ** length

        num //= 10


    if sum == temp:

        print(f"{temp} is armstrong number")    


