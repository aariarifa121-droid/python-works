
#wap to get the count of even and count of digits in given number

number = 1456

odd_count =  0

even_count = 0

while(number > 0):

    digits = number % 10

    if digits % 2 == 0:

        even_count += 1

    else:

        odd_count += 1    

    number = number // 10

print(f"the number of digits {even_count,odd_count}")        

