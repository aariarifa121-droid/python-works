
#display the bonus percentage            
# salaray  bouns
# 50000  20%      
# 30000  10%
# below 30000 5% 

salary = int(input("enter the salary:"))

if salary == 50000:

    bouns = salary * (20 / 100)

    print(f" ur total salary is {salary + bouns}")

elif salary == 30000:

    bouns = salary * (10 / 100)

    print(f" ur total salary is {salary + bouns}")


elif salary < 30000:
   
   bouns = salary * (5 / 100)

   print(f" ur total salary is {salary + bouns}")


else:

    print("thankyou")    

