number = 153

temp = 0

reverse = 0

while(number > 0):

    digits = number % 10

    reverse = reverse * 10 + digits 

    number = number // 10


if temp == reverse:

    print("palindrome")

else:

    print("not palindrome")

