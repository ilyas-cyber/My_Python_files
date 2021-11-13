
       # Water Gun Game #

import random
inp = int(input("Choose your choice:\n1:Snake\n2:water\n3:Gun:\n"))

while(inp<10):
    if (inp == 1):
        list_inged = ["Snake", "water", "gun"]
        choice = random.choice(list_inged)
        if (choice == "water"):
            print("The computers choice",choice)
            print("You Won! Congrats")
        else:
            print("The computers choice",choice)
            print("You Loss! Opps")
    if (inp == 2):
        list_inged = ["Snake", "water", "gun"]
        choice = random.choice(list_inged)
        if (choice == "gun"):
            print("The Computer choice is", choice)
            print("You Won! Congrats")
        else:
            print("The Computer choice is", choice)
            print("You Loss! Opps")
    if (inp == 3):
        list_inged = ["Snake", "water", "gun"]
        choice = random.choice(list_inged)
        if (choice == "gun",):
            print("The Computer choice is", choice)
            print("You Loss! Opps")
        else:
            print("The Computer choice is", choice)
            print("You Won! Congrats")

    break

