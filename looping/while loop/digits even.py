#wap to get the count of even digits from the number given

number = 1463

count = 0

while(number > 0):

    digits = number % 10

    if digits % 2 == 0:

         count += 1

    number =  number // 10

print(f" the even digits {count}")         


