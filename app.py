import random

top_of_range = input("Type a number between 1 and 10: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please Type a number")

random_number = random.randint(0,top_of_range)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("Correct")
            break
        else:
            print("Please type another number")
    else:
        print("Please Enter a number")
