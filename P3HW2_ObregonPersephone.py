#Persephone Obregon
#11-21-23
#Use if/else to determine an employee's pay

#Get input from user
emp_name = input("Enter employee's name: ")
emp_hours = float(input("Enter number of hours worked: "))
emp_pay = float(input("Enter employee's pay rate: "))

#Calculations
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hours = 40
else:      #This represents if emp_hours is 40 or less
    ot_hours = 0
    reg_hours = emp_hours

#Calculate pay
ot_pay = (emp_pay * 1.5) * ot_hours
reg_pay = emp_pay * reg_hours
gross_pay = ot_pay + reg_pay

#Display output
print("-------------------------------------")
print("Hours Worked", "     ", "Pay Rate", "     ", "OverTime", "     ", "OverTime Pay", "     ", "RegHour Pay", "     ", "Gross Pay")
print("-------------------------------------------------------------------------------------------------------")
print(emp_hours, "               ", emp_pay, "        ", ot_hours, "           ", ot_pay, "          ", reg_pay, "            ", gross_pay)
