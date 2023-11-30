#Persephone Obregon
#11-30-23
#Use if/else to determine an employees pay

#Create variables to hold totals paid to employees
total_emp = 0 
total_ot = 0
total_reg = 0
total_gross = 0

#Get input from user
emp_name = input("Enter employee's name or type 'Done' to terminate: ")
#Loop to control adding employees
while emp_name != "Done":
    total_emp += 1
    emp_hours = float(input("Enter employee's hours: "))
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
    total_ot += ot_pay
    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay
    gross_pay = ot_pay + reg_pay
    total_gross += gross_pay

    #Display output
    print("-------------------------------------")
    print("Hours Worked", "     ", "Pay Rate", "     ", "OverTime", "     ", "OverTime Pay", "     ", "RegHour Pay", "     ", "Gross Pay")
    print("-------------------------------------------------------------------------------------------------------")
    print(emp_hours, "               ", emp_pay, "        ", ot_hours, "           ", ot_pay, "          ", reg_pay, "            ", gross_pay)
    print()
    emp_name = input("Enter employee's name or type 'Done' to terminate: ")

#This code executes after the loop breaks
print("Done adding employees")
print()
print(f"Total number of employees: {total_emp}")
print(f"Total amount paid for overtime: {total_ot}")
print(f"Total amount paid in regular hours: {total_reg}")
print(f"Total amount paid in gross: {total_gross}")



