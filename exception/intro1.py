
try:
    num1 = int(input("enter number"))
    num2 = int(input("enter numbet"))

    r=num1/num2
    print("result",r)

except ZeroDivisionError:
    print("zero division error")

except ValueError:

    print("value error")

except:
    print("error")            