
num = 153

temp = num

sum = 0

while(num > 0):

    digits = num % 10

    sum += digits ** 3

    num = num // 10

#if sum == temp:

    #print(f"number is armstrong")

#else:

   # print(f"not armstrong number")    


print("armstrong" if sum == temp else "not armstrong")    