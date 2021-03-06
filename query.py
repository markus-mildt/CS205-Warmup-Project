import load_data as db

# team name location
# team name goals
# team "location"
# "player name" team
# "player name" position
# "player name" location  THIS IS THE JOIN FUNCTION
# "player name" goals

def query(index, column, table):
    # query takes 3 arguments
    # index is whatever the user puts between quotes or the name of the team
    # column should correspond with the column of a table
    # if whatever the user requested does not exist query should return -1

    conn = db.load_data()

    #index is the actual input for the query
    #PLAYERS
    if table == "players":
        pass
        if column == "team":
            return get_player_team(index, conn)
        if column == "position":
            return get_player_position(index, conn)
        if column == "location":
            return get_team_location(get_player_team(index, conn), conn) #JOIN query
        if column == "goals":
            return get_player_goals(index, conn)

    #####team "location"
    elif table == "getTeam":
        return get_all_teams_from_location(index, conn)

    ####TEAMS
    else:

        if column == "location":
            return get_team_location(index, conn)
        if column == "goals":
            return  get_team_goals(index, conn)
        if column == "players":
            return get_all_players_from_team(index, conn)



def get_player_team(player_name, conn):
    # format query from arg
    #check if there is a connection
    if conn is None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    #create cursor object
    cur = conn.cursor()

    # SQL
    query = "SELECT DISTINCT player_team FROM Players WHERE player_name =?"

    # Executes the selection of a row
    cur.execute(query, (player_name,))

    # fetchall data output as tuple
    query_output = cur.fetchall()
    conn.commit()

    #prints out the tuple if its not empty, else return -1
    if len(query_output) != 0:
        for x in query_output:
            return (x[0])
    else:
        # print("There was nothing to match with your input.")
        return -1

#returns the position of a player
def get_player_position(player_name, conn):
    #check for connection
    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    # cursor object created
    cur = conn.cursor()

    #SQL for selection
    query = '''SELECT DISTINCT current_position FROM Players WHERE player_name = ?'''
    cur.execute(query, (player_name,))

    #puts tuple into query_outpur
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        for x in query_output:
            return (x[0])
    else:
        # print("There was nothing to match with your input.")
        return -1

#returns the location of a team
def get_team_location(team_name, conn):
    # if whatever the user requested does not exist query should return -1
    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = '''SELECT DISTINCT location FROM Teams WHERE team_name = ?'''
    cur.execute(query, (team_name,))
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        for x in query_output:
            return (x[0])  # this value is the location out of the tuple
    else:
        # print("There was nothing to match with your input.")
        return -1

#returns the number of goals a team had in regular season
def get_team_goals(team_name, conn):
    # if whatever the user requested does not exist query should return -1
    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = '''SELECT DISTINCT total_goals_scored FROM Teams WHERE team_name = ?'''
    cur.execute(query, (team_name,))
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        for x in query_output:
            return (x[0])
    else:
        # print("There was nothing to match with your input.")
        return -1

    # conn.commit()

#returns the number of goals a player had in regular season
def get_player_goals(player_name, conn):
    # if whatever the user requested does not exist query should return -1
    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = '''SELECT DISTINCT individual_goals_scored FROM Players WHERE player_name = ?'''
    cur.execute(query, (player_name,))
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        for x in query_output:
            return (x[0])
    else:
        # print("There was nothing to match with your input.")
        return -1

    # conn.commit()

#returns all teams from one location
def get_all_teams_from_location(location, conn):
    # if whatever the user requested does not exist query should return -1
    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = "SELECT DISTINCT team_name FROM Teams WHERE location =?"
    cur.execute(query, (location,))
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        # Will alwyas return more than one so print out the whole tuple
        return query_output
    else:
        # print("There was nothing to match with your input.")
        return -1

#returns all players on a team
def get_all_players_from_team(player_team, conn):
    # if whatever the user requested does not exist query should return -1

    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = "SELECT DISTINCT player_name FROM Players WHERE player_team =?"
    cur.execute(query, (player_team,))
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        # Will alwyas return more than one so print out the whole tuple
        return query_output
    else:
        # print("There was nothing to match with your input.")
        return -1

def get_player_stats(player_name, conn):
    # if whatever the user requested does not exist query should return -1
    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = "SELECT DISTINCT player_name, player_team, current_position, individual_goals_scored " \
            "FROM Players WHERE player_name =?"
    cur.execute(query, (player_name,))
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        #Will alwyas return more than one so print out the whole tuple
        return query_output
    else:
        # print("There was nothing to match with your input.")
        return -1

def get_team_stats(team_name, conn):
    # if whatever the user requested does not exist query should return -1
    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = "SELECT DISTINCT team_name, location, total_goals_scored " \
            "FROM Teams WHERE team_name =?"
    cur.execute(query, (team_name,))
    query_output = cur.fetchall()
    conn.commit()

    if len(query_output) != 0:
        # Will alwyas return more than one so print out the whole tuple
        return query_output
    else:
        # print("There was nothing to match with your input.")
        return -1

def test():
    conn = db.load_data()
    passed = True

    # True
    if (get_player_team("Jack Eichel", conn) == "Buffalo Sabres"):
        passed = True
    else:
        passed = False

    #True
    if (get_player_position("Jack Eichel", conn) == "Center"):
        passed = True
    else:
        passed = False

    # True
    if (get_team_location("Buffalo Sabres", conn) == "New York"):
        passed = True
    else:
        passed = False

    # True
    # tests a players location
    if (get_team_location(get_player_team("Jack Eichel", conn), conn) == "New York"):
        passed = True
    else:
        passed = False

    # True
    if (get_team_goals("Buffalo Sabres", conn) == 193):
        passed = True
    else:
        passed = False

    # True
    if (get_player_goals("Jack Eichel", conn) == 36):
        passed = True
    else:
        passed = False

    # True
    if ('Jack Eichel', 'Buffalo Sabres', 'Center', 36) in get_player_stats("Jack Eichel", conn):
        passed = True
    else:
        passed = False

    # True
    if ('Buffalo Sabres', 'New York', 193) in get_team_stats("Buffalo Sabres", conn):
        passed = True
    else:
        passed = False

    #return boolean
    return passed