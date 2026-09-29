#wap to reverse the number enter by user

number = 153

reverse = 0

while(number > 0):

    digits = number % 10

    reverse = reverse * 10 + digits 

    number = number // 10

print(reverse)    