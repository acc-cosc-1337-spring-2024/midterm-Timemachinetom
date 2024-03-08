import question_d 
import random

exit = False

while exit != True:
    play = input ("Welcome! I will pick a number between 1 and 5. If you can guess the number, you will win a fabulous prize! Would you like to play? Please enter Yes or No.")
    if play == "Yes":
        game = True
        while game != False:
            correct = False
            n = question_d.get_random_number()
            print (n)
            while correct != True:
                guess = int(input ("Enter your guess."))
                if guess == n:
                    play_again = input ("Congratulations! Your prize is the valuable knowledge that you were correct! Would you like to play again? Yes or No.")
                    if play_again == "Yes":
                        correct = True
                    if play_again == "No":
                        game = False
                        exit = True
                        correct = True
                else:
                    print ("Incorrect! Guess again!")
    if play == "No":
        exit = True
if exit == True:
    print ("Goodbye")