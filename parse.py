from query_test import query_test
def parse():
    parsing = True
    while parsing:

        waiting_for_input = True
        while waiting_for_input:
            query_input = ""
            query_input = input("Enter Query\n")
            #get input from keyboard
            #validate
            valid = True
            if valid:
                waiting_for_input = False
            else:
                pass

        #call query function with valid input
        query_return = query_test("'Jack Eichel' position")

        #format and print output from query function
        print(query_return)
