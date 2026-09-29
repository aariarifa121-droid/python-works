
#wap to get the mark from the student
# if the mark is above 90 and less than or equal to 100 "a grade"
# if the mark is abive 80 and less than or equal to 90 "b grade"
#if the mark is abive 60 and less than or equal to 80 "c grade"
#below 60 failed

mark = int(input("enter the mark: "))

if mark > 90:

    if mark <= 100:

        print("A grade")

elif mark > 80:

    if mark <= 90:

        print("B grade")

elif mark >= 60:

    if mark <= 80:

        print("c grade")

else:
    print("sorry u are failed")                        