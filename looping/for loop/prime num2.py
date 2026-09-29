
num = int(input("enter the number: "))

while(num <= 1):

    num = int(input("enter the number: "))

for i in range(2 , num):

    if num % i == 0:

        print(f"{num} is not prime")

        break
else:

    print(f"{num} is prime")
        
