# print the odd number count from 1 to n

count = 0

n = int(input("enter the number"))

for i in range(1, n + 1):

    if i % 2 != 0:

        count += 1

        print(i)


