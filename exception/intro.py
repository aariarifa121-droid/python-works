
try:
    num1 = int(input("enter number"))
    num2 = int(input("enter numbet"))

    s=num1+num2

except:
    print("invalid number")

else:
    print("sum",s)

finally:
    print("done")            