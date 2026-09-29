# wap to the print the cube of odd numbers from  n to m

n = int(input("enter the number: "))

m = int(input("enter the number: "))

while(n <= m):

    if n % 2 != 0:

        print(n ** 3)

    n += 1    