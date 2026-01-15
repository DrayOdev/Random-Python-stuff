# text based adventure game idk how to story so uh no story just flex

from venv import create

# AN IDENTIATION IS 3 SPACES
#   indent
#   4 spaces
score = create("Points")

def textbasedadventure():
    # start out by getting username
    # one time event to introduce and do the above

    # local variables
    hpb: bool = False # has programmed in python before
    points: int = 0

    score = open('Points.txt', 'w')

    # > INTRO SEGMENT START
    name = input("Please input your username: ")
    check = input("Welcome, " + name + "\nTo clarify this is the name you would like to continue with [y/n] ")
    if check.lower() == "y":
        print("Great! Lets continue then!")
    elif check.lower() == "n":
        name = input("Please input your username: ")
    print("Lets proceed! Are you ready ", name + "?")
    # > INTRO SEGMENT END
    # > QUESTION 1 START
    q1 = input("Have you ever programmed in python before? [y/n] ")
    if q1.lower() == "y":
        print("Amazing! lets begin with some programming!")
        hpb = True
    elif q1.lower() == "n":
        print("Okay, that's fine. Lets ease you into it!")
    # > QUESTION 1 END
    # > BRANCH 1 HPB IS TRUE
    if hpb == True:

        q2 = input("Would you like to start with code correction? [y/n] ")
        if q2.lower() == "y":
            print("Amazing choice", name + "!", "Lets begin"  )
            print("# BEGIN CODE SEGMENT\ndef func():\n   name = question(\"What is your name: \")\n   if name != \"\"\n      # Proceed with code")
            print("What are the mistakes with the code segment above?")
            q2_1 = input()
            if "input" in q2_1.lower():
                print("Well done! +1 point")
                points += 1
            else:
                q2_1_1 = input("Oooo, not quite, try again? [y/n] ")
            if points != 1:
                if q2_1_1.lower() == "y":
                    print("Okay!")
                    q2_1 = input()
                    if "input" in q2_1.lower():
                        print("Well done!")
                    else:
                        print("Ah not quite, okay so the mistake was the use of \"question\" the correct method name is \"input\"")
            if points == 1:
                print("Okay, that was too easy, lets ramp up the difficulty for ya a bit.")
                print("# BEGIN CODE SEGMENT\nfrom venv import create\nname = \"\"\nage = 0\nFavFilm = \"\"\nnewfile = create(\"file\")\ndef questions():\n   # What should go here?")
                print("   age = questions(\"what is your age?\")\n   # What goes here?")
                


    # > BRANCH 1 END
    # BRANCH 1 HPB IS FALSE
    if hpb == False:
        print("UNDER CONSTRUCTION PLEASE CHECK AGAIN LATER :3")
    # > BRANCH 1 END
    score.write("your total number of points is: " + str(points))
    score.close()



def intro():
    print("#---------------------------------------------------------------------------------------------#")
    print("Welcome to this text based adventure game! This game will showcase some cool python stuff!")
    print("You'll be given the opportunity to try and write your own code and have this program run it!")
    print("#---------------------------------------------------------------------------------------------#")
    textbasedadventure()

intro()
