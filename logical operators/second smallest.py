
#wap to check the second smallest number amoung three

num_1 = int(input("enter the number: "))

num_2 = int(input("enter the number: "))

num_3 = int(input("enter the number: "))

if num_1 < num_2 and num_1 > num_3 or num_1 > num_2 and num_1 < num_3:

    print(f"{num_1} second smallest")

elif num_2 < num_1 and  num_2 > num_1 or num_2 > num_1 and num_2 < num_3:

    print(f"{num_2} second smallest")

else:

    print(f"{num_3} second smallest")

