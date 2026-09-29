# perfect number

# a positive whole number that equals the sum of its proper positive factors

#wap to check the given number is perfect or not

# number = 8

# range (1, number) # 1,2,3,4,5,6,7

## 8 >>>> 1,2,4

## 6 >>>> 1,2,3 1 + 2 + 3 6

number = 6

sum =0

for i in range(1, number):

    if number % i == 0:

        sum += i

    if sum == number:

        print("perfect")

    else:

        print("not perfect")