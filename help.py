# calls help, just a bunch of print statements detailing how to use our program

def help():

    answer = input("What do you need help with? Press 1 for a summary of our program, 2 for how to use the commands, or 3 to quit: ")
    valid = False
    valid2 = False

    while valid2 == False:
        while valid == False:
            if answer == "1" or answer == "2" or answer == "3":
                valid = True
            else:
                answer = input("Please enter a valid response: ")

        if answer == "1":
            print("You have accessed the summary. better write a summary now lol...")
            answer = input("Do you need anymore help? (1,2,3): ")
            if answer != "1" or answer != "2" or answer != "3":
                valid = False
        elif answer == "2":
            print("Ok now write all the commands lol..")
            answer = input("Do you need anymore help? (1,2,3): ")
            if answer != "1" or answer != "2" or answer != "3":
                valid = False
        elif answer == "3":
            print("Thank you.")
            valid2 = True