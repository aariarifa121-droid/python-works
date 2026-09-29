#Print all numbers whose square ends with digit 6 from 1 to 100.


for i in range(1 , 101):
    
    if (i ** 2) % 10 == 6:
        
        print(i)