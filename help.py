# calls help, just a bunch of print statements detailing how to use our program

def help():

      print("Hello! Welcome to our CS205 Warmup Project.  For this projects, we have created"
          "a command-line interface to query data from a database of hockey teams and players.")

      print("Here are the commands for players:")
      print("\"player name\" location\"")
      print("\"player name\" team\"")
      print("\"player name\" position\"")
      print("\"player name\" goals\"")
      print("For example, in the console you would input: \"Jack Eichel\" team")
      print("This will give the output Buffalo Sabers. Note that the player name must be in quotation"
            "marks in order to work.")

      print("")
      print("Here are the commands for teams:")
      print("team location\"")
      print("team goals\"")
      print("For example, in the console you would input: Buffalo Sabres goals")
      print("This will give the input 193.  Note that the team name is NOT in quotation marks.")
      print("In addition, we have a commands that gets all of the teams in one location:")
      print("Team Name \"location\"")
      print("For example, in the console you would input: team \"Canada\"")
      print("This will give the Edmonton Oilers.")

      print("")
      print("Finally, we have a command for load data and quit.")
      print("If you have any quesitons, please contact our technical support team. Happy querying!")

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