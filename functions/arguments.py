
#define a function to get the sum of numbers 

def sum_numbers(*args):

    sum = 0

    for i in args:


        sum += i

    print(sum) 


sum_numbers(3,4,5,6,7)
sum_numbers(3,4,5,)
sum_numbers(3,4,)


def details(**kwargs):  #used to accept different number of keyword arguments

    print(kwargs) #{'name': 'sukumar', 'age': 27, 'place': 'kochi'}


details(name = "sukumar", age = 27, place ="kochi")

#list, set,, dictionary ,tuple
#methods