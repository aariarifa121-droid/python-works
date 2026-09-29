#Eligible for Exam: Take attendance and marks. Eligible if attendance>=75 AND
#marks>=40.

attendance = int(input("Enter attendance percentage: "))

marks = int(input("Enter marks: "))

if attendance >= 75 and marks >= 40:

    print("Eligible")

else:
    
    print("Not Eligible")