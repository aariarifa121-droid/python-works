 #Print numbers where from 1 to 100


for i in range(1 , 101):

    n = i
    
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10

    if i == sum ** 2:
        print(i)