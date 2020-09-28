from query_test import query_test
import help
import load_data
def parse():
    parsing = True
    while parsing:

        waiting_for_input = True
        while waiting_for_input:
            # "player name" team
            # "player name" position
            # "player name" location
            # "player name" goals
            # team name "location"
            # team name goals
            # team "location"

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

            index = ""
            column = ""
            table = ""
            query_return = ""

            ###########
            # testing, delete later
            ##########
            #query_input = "team \"New York\""
            ##########
            # Testing, delete later
            #########


            ###
            # getting the stuff between quotes if there are quotes
            ###
            quote_start = query_input.find("\"")

            # "player name" team
            # "player name" position
            # "player name" location
            # "player name" goals
            if quote_start == 0:
                table = "players"
                quote_end = query_input.find("\"", quote_start+1)

                if quote_end != -1:
                    index = query_input[quote_start+1:quote_end]
                    print(user_specified_string)
                    # Gets whatever is after the quotes
                    column = query_input[quote_end:]

                    if column in valid_columns:
                        query_return = query_test(index, column, table)
                        if query_return == -1:
                            print("We could not find that player's " + column)
                            print("Remember input is case sensitive and try again, or try another query")
                            query_return = ""

            # team name location
            # team name goals
            # team "location"
            else:
                # team "location"
                if query_input[0:4] == "team":
                    if query_input[5:6] == " \"" and query_input[-1] == "\"":

                        index = query_input[6:-2]
                        column = "location"
                        table = "teams"
                        query_return = query_test(index, column, table)
                        if query_return == -1:
                            print("We could not find a team at that location, remember that input is case-sensitive and try again, or try another query. Type help for help")
                            query_return = ""
                    else:
                        print("1")
                else:
                    # getting the index where the second space in the query is
                    column_start = query_input.find(" ", query_input.find(" ") + 1)
                    if column_start == -1:
                        print("Your query cannot be recognized, type help for help")
                    else:
                        index = query_input[:column_start]
                        column = query_input[column_start:]
                        table = "teams"
                        query_return = query_test(index, column, table)
                        if query_return == -1:
                            print("We could not find information about that team, remember input is case sensitive, type help for help")
                            query_return = ""

            if query_return == -2:
                print("The database has not been loaded yet, please use the command load data")


            print(query_return)