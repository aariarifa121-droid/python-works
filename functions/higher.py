#create a new list of squares


l = [1,2,3,4]

print(list(map(lambda x: x**2,l)))
print(set(map(lambda x: x**2,l)))
print(tuple(map(lambda x: x**2,l)))

