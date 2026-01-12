#-------------------------------#
#----------PASSWORDGEN----------#
#-------------------------------#
import random as random
from venv import create
import os
passwords = create("PASSES")
AlphabetLower = list("abcdefghijklmnopqrstuvwxyz")
AlphabetUpper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = list(r"\'!@#$%^&*()[]{}?:;~`¬_-+=/|")
Numbers = list("0123456789")

def startup():
    print("Welcome to the ultimate password generator, a password is being generated...")
startup()

def main():
    # generate a password of a decent length probably 32 character, ensure that it uses a mix of everything
    # do not make it balanced out. Using a for loop and random value I can pick what to append next
    passwords = open('PASSES.txt', 'w')
    password = ""
    for i in range(32):
        chance = random.randint(1,4)
        match chance:
            case 1:
                password = password + AlphabetUpper[random.randint(0, len(AlphabetUpper)-1)]
            case 2:
                password = password + AlphabetLower[random.randint(0, len(AlphabetLower)-1)]
            case 3:
                password = password + Numbers[random.randint(0, len(Numbers)-1)]
            case 4:
                password = password + special_characters[random.randint(0, len(special_characters)-1)]

    print("The password has been stored in a newly created file:", os.path.abspath("PASSES.txt"))
    print("This will be overwritten if you run the program again.")
    passwords.write(password)
    passwords.close()
    passwords = open('PASSES.txt', 'r')
    read = passwords.readlines()
    PASS = read[0]
    print(PASS)
    passwords.close()

    ask = input("Do you want to generate a new password? (y/n) ")
    match ask:
        case "y":
            main()
        case "n":
            print("Closing the program...")
        case _:
            print("Sorry, unrecognized answer")
            asking()
main()

def asking():
    ask = input("Do you want to generate a new password? (y/n) ")
    match ask:
        case "y":
            main()
        case "n":
            print("Closing the program...")
        case _:
            print("Sorry, unrecognized answer")
            asking()
