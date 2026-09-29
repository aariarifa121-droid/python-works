#wap to get the sum of eeven digits of the number

number = 12567

sum = 0

while(number > 0):

    digits = number % 10

    if digits % 2 == 0:

        sum += digits
        
    number = number // 10

print(f"sum of digits {sum}")        

