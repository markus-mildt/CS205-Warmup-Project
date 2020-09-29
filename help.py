# calls help, just a bunch of print statements detailing how to use our program

def help():

    print("Hello! Welcome to our CS205 Warmup Project.  For this projects, we have created \n"
          "a command-line interface to query data from a database of hockey teams and players.\n"
          "To retrieve data about the players, use the commands: location, team, position, and goals.\n"
          "For example, your command may look like this: 'Player Name' team. This will return what\n"
          "team the player is on.  To retrieve data about the teams, use the commands: location and\n"
          "goals.  For example, your command may look like this: 'Team Name' goals.  This will \n"
          "return the total number of goals a team has scored.  Additionally, you can use the command:\n"
          "Team Name 'location', which will return all of the teams in a given location.  An example\n"
          "would be: Team Name Vermont, which would return all of the teams in Vermont. Thank you for\n"
          "reading.  If you have any quesitons, please contact our technical support team. Happy querying!")







    # answer = input("What do you need help with? Press 1 for a summary of our program, 2 for how to use the commands, or 3 to quit: ")
    # valid = False
    # valid2 = False
    #
    # while valid2 == False:
    #     while valid == False:
    #         if answer == "1" or answer == "2" or answer == "3":
    #             valid = True
    #         else:
    #             answer = input("Please enter a valid response: ")
    #
    #     if answer == "1":
    #         print("You have accessed the summary. better write a summary now lol...")
    #         answer = input("Do you need anymore help? (1,2,3): ")
    #         if answer != "1" or answer != "2" or answer != "3":
    #             valid = False
    #     elif answer == "2":
    #         print("Ok now write all the commands lol..")
    #         answer = input("Do you need anymore help? (1,2,3): ")
    #         if answer != "1" or answer != "2" or answer != "3":
    #             valid = False
    #     elif answer == "3":
    #         print("Thank you.")
    #         valid2 = True