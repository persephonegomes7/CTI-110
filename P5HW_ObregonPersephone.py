#Persephone Obregon
#12-7-23
#Use functions, random numbers, and while loops

#Import random library
import random

#This function displays the main menu
def show_menu():
    print("Welcome to Math Quiz")
    print()
    print("MAIN MENU")
    print("------------------------------")
    print("1. Adding random numbers")
    print("2. Subtracting random numbers")
    print("3. Exit")

#This function adds two random numbers
def add():
    rand1 = random.randint(0, 10)
    rand2 = random.randint(0, 10)
    print(f"{rand1} + {rand2}")
    return(rand1 + rand2)

#This function subtracts two random numbers
def subtract():
    rand1 = random.randint(0, 10)
    rand2 = random.randint(0, 10)
    print(f"{rand1} - {rand2}")
    return(rand1 - rand2)

#This function simulates the user guessing
#While the guess is wrong, allow the user to guess again
def guessing(guess, correct_answer):
    num_guesses = 0
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer:  #If user guesses too high
            print("Your guess is too high")
            guess = int(input("Guess again: "))   #Represents guess
        else:                       #If user guesses too low
            print("Your guess is too low")
            guess = int(input("Guess again: "))   #Represents guess
    #User answer is correct, the while loop breaks        
    print("Your answer is correct!!!!")
    print(f"It took you {num_guesses} incorrect guesses to get it right")
    

#Main funtion
def main():
    show_menu()
    user_option = int(input("Please choose one of the menu options: "))
    while user_option != 3:
        if user_option == 1:
            rand_sum = add()    #represents the correct answer
            my_guess = int(input("What is your guess? "))   #Represents guess
            guessing(my_guess, rand_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options: "))
        if user_option == 2:
            rand_subtract = subtract()  #represents the correct answer
            my_guess = int(input("What is your guess? "))   #Represents guess
            guessing(my_guess, rand_subtract)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options: "))
            
    #If user_choice == 3, the while loop breaks
    print("Thank you for playing, goodbye!")
                      
#Call the main function
if __name__ == "__main__":
    main()



