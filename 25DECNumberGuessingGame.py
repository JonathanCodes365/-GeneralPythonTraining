#Here, we will do the number guessing game .

#so, at starting we would always want to import the random module.
#why? Because we simply want to generate a random number that we would want the system to detect.

import random
#Now, we will generate a random number between 1 to 100.
number_to_guess= random.randint(1,100)
#what randint does is it generates a random integer between the random number we provide it.
#random in Line-8 is the random module that we just imported.

#Now, we would also want to keep count of the number of attempts the user has made to guess the number.
attempts = 0
#Now, we will similarly also create a while loop that will keep running until the user guesses the correct number.
while True:
    #Now, let us ask the user to input their guess.
    user_guess = int(input("Enter your guess number between 1 to 100:"))
    attempts +=1 #counting the number of attempts made by the user.
    #Now, we would also want to tell the user if their guess is too high or too low .   
    if user_guess<number_to_guess:
        print("Your guess is too low. Try again!")
        #why we dont use elseif instead of elf is because python does not have elseif keyword.
    elif user_guess>number_to_guess:
        print("Your guess is too high.TRY AGAIN!!")
    else:
        print(f"Congratulations! You've guessed the number succesffully in {attempts} attempts.")
        break
        #the break statement will exit the while loop once the user has guessed the correct number.
#And that's it! You've created a simple number guessing game in Python.
