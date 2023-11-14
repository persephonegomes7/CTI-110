#Persephone Obregon
#11/14/23
#Use float values to represent the cost to drive a specified distance

#Get input from user
mpg = float(input("Enter the car's mpg as a decimal number: "))
cost_gal = float(input("Enter the cost for 1 gallon of gas: "))

#Calculate the cost to drive 20 miles
drive_cost_20 = (20/mpg) * cost_gal

#Calculate the cost to drive 75 miles
drive_cost_75 = (75/mpg) * cost_gal

#Calculate the cost to drive 500 miles
drive_cost_500 = (500/mpg) * cost_gal

#Output the cost to drive 20 miles with 2 decimal places using a f-string
print(f"Cost to drive 20 miles is {drive_cost_20:.2f}")

#Output the cost to drive 75 miles with 2 decimal places using a f-string
print(f"Cost to drive 75 miles is {drive_cost_75:.2f}")

#Output the cost to drive 500 miles with 2 decimal places using a f-string
print(f"Cost to drive 500 miles is {drive_cost_500:.2f}")
