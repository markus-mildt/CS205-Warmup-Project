from query_test import query_test
import help
import load_data
def parse():
    parsing = True
    while parsing:

        waiting_for_input = True
        while waiting_for_input:
            # get input from keyboard
            query_input = ""
            query_input = input("Enter Query\n")


            #validate
            valid = False

            if (query_input == "help"):
                help.help()

            #load data
            if (query_input == "load data"):
                load_data()

            #"player name" location
            #"team name" location
            #"player name" team
            #"Player name" position

            #"team name" goals
            #"player name" goals
            #team "location"

            if valid:
                waiting_for_input = False
        #call query function with valid input
        query_return = query_test("'Jack Eichel' position")

        #if(query_return) returns valid:
        print(query_return)
        #else:
            #print error message
        #format and print output from query function

