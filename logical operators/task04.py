
# wap to check the largest number amoung three

num_1 = int(input("enter the number: "))

num_2 = int(input("enter the number: "))

num_3 = int(input("enter the number: "))

if num_1 > num_2 and num_1 > num_3:

    print(f"{num_1} is the largest")

elif num_2 > num_1 and num_2 > num_3:

    print(f"{num_2} is the largest")

else:

    print(f"{num_3} is the largest")