#wap to get the palindrome num from 1 to 1000

for num in range(1,1001):

    temp = num

    reverse = 0

    while(num > 0):

        digits = num % 10

        reverse = reverse * 10 + digits 

        num //= 10

    if temp == reverse:

        print(f"{temp} is palindrome")