# 
# wap to get the factors of the number 

number = int(input("enter the number: "))

for i in range(1 , number ,+1):
    if number % i == 0:

        print(i)
