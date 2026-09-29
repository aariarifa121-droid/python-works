# wap to get the sum of odd factprs of the number given


sum = 0

number = 12

for i in range(1 , number ):

    if number % i == 0 and i % 2 != 0:

        sum += i

print(f"Sum of odd factors {sum}")