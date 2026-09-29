#wap to get the count of number divisible by 7 from 1 to 50

count = 0

for i in range(1,51):

    if i % 7 == 0:

        count += 1

print(count)        