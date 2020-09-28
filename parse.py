from query_test import query_test
import help
import load_data
def parse():
    parsing = True
    while parsing:

        waiting_for_input = True
        while waiting_for_input:
            # "player name" team
            # "Player name" position
            # "team name" goals
            # "player name" goals
            # team "location"
            # "player name" location
            # "team name" location

            valid_columns = ["team", "position", "goals", "location"]
            # get input from keyboard
            query_input = ""
            query_input = input("Enter Query\n")

            valid = False

            if (query_input == "help"):
                help.help()

            #load data
            if (query_input == "load data"):
                load_data.load_data()

            ###
            # getting the stuff between quotes if there are quotes
            ###
            quote_start = query_input.find("\"")
            if(quote_start == 0):
                quote_end = query_input.find("\"", quote_start+1)
                if(quote_end != -1):
                    index = query_input[quote_start+1:quote_end]
                    print(user_specified_string)
                    column = query_input[quote_end:]
                    if column in valid_columns:
                        valid = True

            # Gets whatever is after the quotes



            if valid:
                waiting_for_input = False
            else:
                print("Invalid Query, type help for help")

        #call query function with valid input
        # query_return = query(index, column)
        query_return = query_test("'Jack Eichel' position")

        if(query_return == -1):
            print("Invalid Query")
        print(query_return)
        #else:
            #print error message
        #format and print output from query function

