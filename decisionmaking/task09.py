#Largest of Two Numbers: Take two numbers. Print the largest or Both are Equal.

num_1 = int(input("enter the number: "))

num_2 = int(input("enter the number: "))

if num_1 > num_2:

    print(f"{num_1} is largest")

elif num_2 > num_1:

    print(f"{num_2} is largest")

else:
    print("both are equal")    
