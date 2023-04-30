# Name: omwira nkere
# Program Purpose: Pordle (PVCC Wordle): Word Guessing Game
#   The program chooses a random word from a file of words. The user tries to
#   figure out the word in the fewest guesses by guessing letters in the word.
#    This program uses an input FILE, LISTS, and STRING SLICES (section of the string)

import random

def main():
    wordList = []
    inFile = "animals.txt"

    def printHeadings():
        print("\nWelcome to PORDLE! The PVCC Wordle Game")
        print("I will think of a word and you try to guess the letters in the word.")
        print("The number of dashes indicates the number of letters in the word.")

    def printMenu():
        nonlocal inFile
        print("Choose a PORDLE category:")
        print("\t1. Animals")
        print("\t2. Chakula")
        print("\t3. Gari")
        print("\t4. Mazoezi")
        category = input("Please enter the category number: ")

        if category == "1":
            inFile = 'animals.txt'
        elif category == "2":
            inFile = 'chakula.txt'
        elif category == "3":
            inFile = 'gari.txt'
        elif category == "4":
            inFile = 'mazoezi.txt'
        else:
            inFile = 'animals.txt'
            print("This will be an ANIMAL PORDLE.")

    def playGame():
        nonlocal wordList
        numguesses = 1
        lettersUsed = []

        wordFile = open(inFile, "r")  # Open the file for READ
        for textLine in wordFile:  # Read in a line of text from the file
            for word in textLine.split():  # Split the line of text into words
                wordList.append(word.lower())  # Add each word to the word list
        wordFile.close()

        wordChosen = random.choice(wordList)
        pordle = "_" * len(wordChosen)
        print(pordle)

        while pordle != wordChosen:  # Keep asking the player until player guesses the word
            letterGuess = input("Please enter a letter: ").lower()
            while letterGuess in lettersUsed:  # Check if the letter has been used before
                print("You have already used this letter. Please try again.")
                letterGuess = input("Please enter a letter: ").lower()
            lettersUsed.append(letterGuess)  # Add the players' letter to the list of guessed letters
            print("Number of guesses: " + str(numguesses))

            for i in range(len(wordChosen)):  # Search through the letters to find a match
                if wordChosen[i] == letterGuess:
                    pordle = pordle[:i] + letterGuess + pordle[i+1:]

            print("Used letters: ")
            print(lettersUsed)
            print(" ".join(pordle))  # Print the string with guessed letters with spaces in between
            numguesses += 1

        print("Well done! You guessed in " + str(numguesses-1) + " guesses!")

    printHeadings()
    playAgain = True
    while playAgain:
        printMenu()
        playGame()
        yesno = input("Would you like to play again? (Y/N)")
        if yesno.lower() == "n":
            playAgain = False
            print("Thank you for playing PORDLE!")

if __name__ == "__main__":
    main()
