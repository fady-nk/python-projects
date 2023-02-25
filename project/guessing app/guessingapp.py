import random

def guessing_game(guessLimit, number):
    random_number = random.randint(1, number)
    try:
        while guessLimit > 0:
            guess = int(input("what is your guess?"))
            guessLimit -= 1
            if random_number == guess:
                print("congrats! you guessed the number")
                break
            elif guess >number:
                print("your guess is out of range")
                print(f"you have {guessLimit} guesses left")
            else:
                print("sorry, that is not the number")
                print(f"you have {guessLimit} guesses left")
            print("game over")
            print(f"the number was {random_number}")
    except ValueError:
            print("only integers are allowed")

def easy():
    print("you are to guess a number between 1 and 10, and you have 6 guesses") 
    guessing_game(6, 10)

def medium():
    print("you are to guess a number between 1 and 20, and you have 4 guesses") 
    guessing_game(4, 20)

def hard():
    print("you are to guess a number between 1 and 50, and you have 3 guesses") 
    guessing_game(3, 50)

def try_again():
    again= input("do you want to play again? (Yes/No)")
    if again.upper() == "YES":
        welcome()
    elif again.upper() == "NO":
        print("thanks for playing")
    else:
        print("invalid input")
        try_again()

def welcome():
       
        print("welcome to the guessing game")
        difficulty = input("choose a difficulty: easy, medium, hard")
        if difficulty.upper() == "EASY":
            easy()
            try_again()
        elif difficulty.upper() == "MEDIUM":
            medium()
            try_again()
        elif difficulty.upper() == "HARD":
            hard()
            try_again()
        else:
            print("invalid input")
            welcome()           

welcome()