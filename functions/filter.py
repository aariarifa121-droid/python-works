
l =[1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x :x%2==0,l)))
print(list(filter(lambda x :x%5==0,l)))

#given a list

l=[23,65,89,12,20,33,85,40]

#filter elements greater than 50

print(list(filter(lambda x:x>50,l)))

#filterneven values less than 50

print(list(filter(lambda x:x%2==0 and x<50,l)))

#given list

l = ['apple','orange','pineapple','grapes','avacado']

print(list(filter(lambda x:len(x),l)))

#filter the elemnts whose lenghth greater than 5
l = ['apple','orange','pineapple','grapes','avacado']


print(list(filter(lambda x:len(x)>5,l)))

