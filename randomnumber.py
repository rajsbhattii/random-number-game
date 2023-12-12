import random

def menu():
    print("Welcome to Numbers at Random!")
    print("1. Play a preset game")
    print("2. Custom settings")
    print("3. Exit")
    menuOption = int(input("Please select an option using the numbers: "))
    if menuOption == 1:
        print("Option 1 selected\n")
        preset()
    elif menuOption == 2:
        print("Option 2 selected\n")
        custom()
    elif menuOption == 3:
        print("Option 3 selected. Thank you for playing!\n")
    else: 
        print("Sorry, invalid selection! Select a valid option.\n")
        menu()

def preset():
    print("Difficulty Levels:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. EXTREME")
    print("5. Return")
    difficulty = int(input("Please select a difficulty using the numbers: "))
    if difficulty == 1:
        lowerBound = 0
        upperBound = 10
        print("Range: " + str(lowerBound) + " to " + str(upperBound))
        computerSelected = random.randint(lowerBound, upperBound)
        guessing(computerSelected)
    elif difficulty == 2:
        lowerBound = 0
        upperBound = 50
        print("Range: " + str(lowerBound) + " to " + str(upperBound))
        computerSelected = random.randint(lowerBound, upperBound)
        guessing(computerSelected)
    elif difficulty == 3:
        lowerBound = 0
        upperBound = 100
        print("Range: " + str(lowerBound) + " to " + str(upperBound))
        computerSelected = random.randint(lowerBound, upperBound)
        guessing(computerSelected)
    elif difficulty == 4:
        lowerBound = 0
        upperBound = 200
        print("Range: " + str(lowerBound) + " to " + str(upperBound))
        computerSelected = random.randint(lowerBound, upperBound)
        guessing(computerSelected)
    elif difficulty == 5:
        print("Returning to previous menu\n")
        menu()
    else:
        print("Invalid selection, please try again")
        preset()

def custom():
    lowerBound = int(input("Enter the lower bound: "))
    upperBound = int(input("Enter the upper bound: "))
    if lowerBound > upperBound:
        computerSelected = random.randint(upperBound, lowerBound)
        print("Range: " + str(upperBound) + " to " + str(lowerBound))
        guessing(computerSelected)
    else:
        computerSelected = random.randint(lowerBound, upperBound)
        print("Range: " + str(lowerBound) + " to " + str(upperBound))
        guessing(computerSelected)

def guessing(computerSelected):
    guesser = int(input("Guess the number selected between the range specified: "))
    while guesser != computerSelected:
        if guesser != computerSelected:
            print("Wrong. Try again.")
            guesser = int(input("Guess the number selected between the range specified: "))
    if guesser == computerSelected:
        print("Correct! Great job.\n")
        restart()

def restart():
    print("What would you like to do next?")
    print("1. Exit")
    print("2. Play again")
    selection = int(input("What would you like to do: "))
    if selection == 1:
        print("Thank you for playing")
    elif selection == 2:
        menu()

menu()