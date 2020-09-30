from query_test import query_test
from query import query
import help
import load_data


# Parser Testing:
# team "location":
##correct behavior on good input: yes
# bad input: yes

# team name location:
##correct behavior on good input: yes
# bad input: yes

# team name goals
##correct behavior on good input: yes
# bad input: yes

# "player name" team
##correct behavior on good input:
# bad input:

# "player name" position
##correct behavior on good input:
# bad input:

# "player name" location
##correct behavior on good input:
# bad input:

# "player name" goals
##correct behavior on good input:
# bad input:

def parse():
    print("Welcome to our NHL interface! Type 'help' for suggestions or 'quit' to exit!")
    print("")
    parsing = True
    while parsing:

        waiting_for_input = True
        while waiting_for_input:
            # "player name" team
            # "player name" position
            # "player name" location
            # "player name" goals
            # team name location
            # team name goals
            # team "location"

            valid_columns = ["team", "position", "goals", "location"]
            # get input from keyboard
            print("")
            query_input = ""
            query_input = input("Enter Command\n")

            valid = False

            ###
            # getting the stuff between quotes if there are quotes
            ###
            quote_start = query_input.find("\"")

            index = ""
            column = ""
            table = ""
            query_return = ""

            if query_input == "help":
                help.help()

            # load data
            elif query_input == "load data":
                print("loading data...")
                load_data.load_data()

            # quit the program
            elif query_input == "quit":
                print("Thank you! We hope you return soon!")
                return 0

            ###########
            # testing, delete later
            ##########
            # query_input = "\"Jack Eichel\" team"
            ##########
            # Testing, delete later
            #########


            # "player name" team        teams do NOT start with quotes
            # "player name" position
            # "player name" location
            # "player name" goals
            # print("quote start is " + str(quote_start))

            elif quote_start == 0:
                table = "players"
                quote_end = query_input.find("\"", quote_start + 1)

                if quote_end != -1:
                    index = query_input[quote_start + 1:quote_end]
                    # print(user_specified_string)
                    # Gets whatever is after the quotes
                    column = query_input[quote_end+2:]

                    if column in valid_columns:
                        query_return = query(index, column, table)
                        if query_return == -1:
                            print("We could not find that player's " + column)
                            print("Remember input is case sensitive and try again, or try another query")
                            query_return = ""
                        print(str(query_return))


            # team name location
            # team name goals
            # team "location"
            else:
                # team "location"
                # print("quotestart is: " + str(quote_start))
                if query_input[0:4] == "team":
                    query_input.find(" \"")
                    if query_input[4:6] == " \"" and query_input[-1] == "\"":

                        index = query_input[6:-1]
                        column = "location"
                        table = "getTeam"
                        query_return = query(index, column, table)
                        if query_return == -1:
                            print("We could not find a team at that location, remember that input is case-sensitive and try again, or try another query. Type help for help")
                            query_return = ""
                        print(str(query_return))

                    else:
                        print("Your query cannot be recognized, type help for help")

                else:
                    # team name location
                    # team name goals
                    # getting the index where the second space in the query is
                    for column in valid_columns:
                        column_start = query_input.find(column)
                        # print(column_start)
                        if column_start != -1:
                            break

                    if column_start == -1:
                        print("Your query cannot be recognized, type help for help")

                    else:
                        index = query_input[:column_start - 1]
                        column = query_input[column_start:]
                        table = "teams"
                        query_return = query(index, column, table)
                        if query_return == -1:
                            print("We could not find information about that team, remember input is case sensitive, type help for help")
                            query_return = ""
                        print(str(query_return))