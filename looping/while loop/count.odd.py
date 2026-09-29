#wap to get the count of odd number from 1 to n


i = 1

n = int(input("enter the number: "))

count = 0

while(i <= n):

    if i % 2 != 0:

        count +=1

    i += 1

print(count)        

  