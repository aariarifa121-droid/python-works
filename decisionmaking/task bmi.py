
#bmi = weight_km / (height_m ** 2)
#underweight : bmi less than 18.5
#normal / healthy weight: bmi 18.5 to 24.9
#over weight : we bmi 25.0 to 29.0
#obesitiy : bmi 30.0 or more

weight_kg = float(input("Enter your weight (kg): "))

height_m = float(input("Enter your height (m): "))


bmi = weight_kg / (height_m ** 2)



if bmi < 18.5:

    print("Underweight")

elif bmi >= 18.5 and bmi <= 24.9:

    print("Normal / Healthy Weight")

elif bmi >= 25.0 and bmi <= 29.9:

    print("Overweight")

else:

    print("Obesity")


