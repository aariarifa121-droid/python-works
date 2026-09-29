#write a program  to find the position at a specific character in a string

s = "hello world"

ch="l"


if ch in s:

    print("the position of",ch,"is",s.index(ch))

else:
    print("character",ch,"is not present")

#write  a program to find the count of a specific character in a string

s = "hello world"

ch="l"


if ch in s:

    print("the count of",ch,"is",s.count(ch))

else:
    print("character",ch,"is not present")    


#write a  program to create new dictionary where keys are letter and values
#are the count of each letter

s ="hello world"
new ={}

for i in s:
    if(i.isalpha()):

        new[i]= s.count(i)

print(new)


#Write a program to create a new list with 5 random 3 digit numbers

new = []

import random

for i in range(5):
    num = random.randint(100,1000)

    new.append(num)

print(new)    


#write a program to create a 5 digit otp number


new = []

import random

num = random.randint(10000,99999)



print("the otp num is: ",num)

#write a program to find the count of letters,spaces and digits in a string

s = "hello world 12345"

count_i = 0
count_s = 0
count_d = 0


for i in s:

    if i.isalpha():

        count_i += 1

    elif i.isdigit():

        count_d += 1

    elif i.isspace():

        count_s += 1

        print("letter",count_i)
        print("digits",count_d)
        print("space",count_s)



#write a  program to create new dictionary where keys are words and values
#are the length of each word

new ={}

s ="hello world"
for i in s.split():

    new[i]= len(i)

print(new)


        





