#-----------------------------#
#----------REVERSEIT----------#
#-----------------------------#
import time

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrst")
special_characters = list(r"\'!@#$%^&*()[]{}?:;~`¬_-+=/| ")

def startup():
    print("Hello! Welcome to Text Reverse, enter a string and watch it get reversed!")
startup()

def reverse():
    # functional stuff
    text = input("Enter text to begin: ").lower()
    reversed_text = text[::-1]
    if text == reversed_text:
        print("palindrome detected")
    # visual effects
    listed = list(reversed_text)
    length = len(listed)
    visual = ""
    NumOfVowels = 0
    NumOfConsonants = 0
    NumOfSpecialCharacters = 0
    VowelArray = []
    ConsonantArray = []
    SpecialCharacterArray = []
    for i in range(length):
        if listed[i] in vowels and listed[i] not in special_characters :
            VowelArray.append(listed[i])
            NumOfVowels += 1
        elif listed[i] in consonants and listed[i] not in special_characters:
            ConsonantArray.append(listed[i])
            NumOfConsonants += 1
        elif listed[i] in special_characters:
            SpecialCharacterArray.append(listed[i])
            NumOfSpecialCharacters += 1
        visual = str(visual)
        visual += listed[i]
        time.sleep(.25)
        print(visual)
    print("The number of vowels is: ", NumOfVowels, "\nHere they are: ", VowelArray)
    print("The number of consonants is: ", NumOfConsonants, "\nHere they are: ", ConsonantArray)
    print("The number of special characters is: ", NumOfSpecialCharacters, "\nHere they are: ", SpecialCharacterArray)
    # rerun
    ask = input("Would you like to go again? y/n: ")
    match ask:
        case "y":
            reverse()
        case "n":
            print("Goodbye!")
reverse()
