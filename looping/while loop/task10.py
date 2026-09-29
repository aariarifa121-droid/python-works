
# Ask the user to enter a number. Keep asking until they enter a value over 5 and 
#then display the message “The last number you entered was a [number]” and top the program.

number = int(input("enter the number :"))

while(number <= 5):

    number  = int(input("enter the number :"))

print(f"the last number you entered was a number {number}")