#bmr = (10 * weight in kg ) + (6.25 * height in cm) - (5 * age in years) + 5
#weight_kg
#height_cm
#age

weight_kg = int(input("enter your weight: "))

height_cm = int(input("enter your height: "))

age = int(input("Enter your age (years): "))

bmr = (10 * weight_kg ) + (6.25 * height_cm) - (5 * age) + 5

print(f"your bmr is {bmr}")