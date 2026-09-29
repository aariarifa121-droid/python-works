# Count numbers divisible by 3 but not divisible by 5 from 1 to 50


count = 0

for i  in range(1 , 51):

    if i % 3 == 0 and i % 5 != 0:

        count += 1
        
print(count)        


