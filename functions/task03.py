#define a function that takes a list of numbers as arduments
#and print the count of even number odd numbers and numbers whose value geater than 50
#l = [23,56,12,78,98,89,31,67]

def count_number(num):

    count_e = 0
    count_0 = 0
    count_g = 0

    for i in num:

        if i % 2 == 0:

            count_e += 1

        else:
            count_0 += 1

        if i > 50:
            count_g += 1

    print("Even numbers:", count_e)
    print("Odd numbers:", count_0)
    print("Numbers greater than 50:",count_g)


count_number([23, 56, 12, 78, 98, 89, 31, 67])




