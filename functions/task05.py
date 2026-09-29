
#define a lambda function to find the cube of a number

s = lambda n:n**3

print(s(5))


#sum of 2 numbers 

s = lambda a,b:a+b

print(s(2,5))

#peoduct of 3 numbers

p = lambda a,b,c:a*b*c

print(p(10,5,6))

#length of string

x = lambda n:len(n)

print(x("nandu"))

#square root  of numbers

s = lambda n: n**0.5

print(s(50))

#first letter of a string

x = lambda n:n[0]

print(x("nandu"))

#last letter of a string 

x = lambda n:n[-1]

print(x("anju"))

#name value from dictionary

x = lambda d:d.get("name")

print(x({"name":"amii","place":"ekm"}))

#salary value from dictionary

x= lambda d:d.get("salary")

print(x({"name":"ami","place":"ekm","salary":2300}))

#add 10 to a number
   
x= lambda a:a+10

print(x(6))