#Persephone Obregon
#11/14/23
#Design a program to sort through grades

from statistics import mean

#Get input from the user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

#Create a list to store the grades entered
grades_list = []

#Add values to the list
grades_list.append(grade1)
grades_list.append(grade2)
grades_list.append(grade3)
grades_list.append(grade4)
grades_list.append(grade5)
grades_list.append(grade6)

#Call methods on the list to get results
list_sum = sum(grades_list)
list_avg = mean(grades_list)
lowest_grade = min(grades_list)
highest_grade = max(grades_list)

#Create a value for spacing
x = " "

#Output to user with f-string
print("\n")
print("------------Results------------")
print("Lowest Grade:", '    ', lowest_grade)
print("Highest Grade:", '   ', highest_grade)
print("Sum of Grades:", '   ', f"{list_sum:.2f}")
print("Average:", '         ', f"{list_avg:.2f}")
print("-------------------------------")




