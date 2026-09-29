# Print all numbers that have exactly 4 factors.


for i in range(1, 101):

    count = 0

    for j in range(1, i + 1):

        if i % j == 0:

            count = count + 1

    if count == 4:
        
        print(i)

