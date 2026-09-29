#wap to the perfect numbers from 1 to 1000


for num in range(1,1000):

    sum = 0

    for i in range(1,num):

        if num % i == 0:

            sum += i

    if sum == num:

        print("perfect",num)        


        

