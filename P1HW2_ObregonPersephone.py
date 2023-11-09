#Persephone Obregon
#11/9/2023
#Using integers to create a budget of travel expenses

#State what the program does
print("This program calculates and displays travel expenses")

#Get input from user
number1 = int(input("Enter Budget: "))
location1 = input("Enter your travel destination: ")

number2 = int(input("How much do you think you will spend on gas? "))
number3 = int(input("Approximately, how much will you need for accomodation/hotel? "))
number4 = int(input("Last, how much do you need for food? "))

#Separate to dispay travel expenses
print("------------Travel Expenses------------")

#Display output
print("Location:", location1)
print("Initial Budget:", number1)

print("Fuel:", number2)
print("Accomodation:", number3)
print("Food:", number4)

#Display remaining balance
print("Remaining Balance:", number1 - number2 - number3 - number4)
