
# wap to get the sum of even numbers and product of odd number 1 to n

i = 1

n = int(input("enter the number: "))

sum = 0

product = 1

while(i <= n):

    if i % 2 == 0:

        sum += i

    else:

        product *= 1

    i += 1

print(f"the sum  and product is {sum} , {product}")            
