import load_data as db


def test():
    conn = db.load_data()
    get_player_team("Jack Eichel", conn)
    get_player_position("Jack Eichel", conn)
    get_team_location("Buffalo Sabres", conn)
    get_team_goals("Buffalo Sabres", conn)
    get_player_goals("Jack Eichel", conn)
    get_all_teams_from_location("New York", conn)
    get_all_players_from_team("Buffalo Sabres", conn)


def get_player_team(player_name, conn):
    # query takes 3 arguments
    # index is whatever the user puts between quotes, column is whatever is after the quotes, which is the column of one of the tables
    # table is which table needs to be queried
    # if whatever the user requested does not exist query should return -1

    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = "SELECT DISTINCT player_team FROM Players WHERE player_name =?"
    cur.execute(query, (player_name,))

    # fetchall returns rows as tuples
    output = cur.fetchall()
    conn.commit()

    if len(output) != 0:
        for x in output:
            return (x[0])
    else:
        print("There was nothing to match with your input.")
        return -1

    # conn.commit()

#returns the position of a player
def get_player_position(player_name, conn):
    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = '''SELECT DISTINCT current_position FROM Players WHERE player_name = ?'''
    cur.execute(query, (player_name,))
    output = cur.fetchall()
    conn.commit()

    if len(output) != 0:
        for x in output:
            return (x[0])
    else:
        print("There was nothing to match with your input.")
        return -1

    # conn.commit()

#returns the location of a team
def get_team_location(team_name, conn):
    # if whatever the user requested does not exist query should return -1

    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = '''SELECT DISTINCT location FROM Teams WHERE team_name = ?'''
    cur.execute(query, (team_name,))
    output = cur.fetchall()
    conn.commit()

    if len(output) != 0:
        for x in output:
            return (x[0])
    else:
        print("There was nothing to match with your input.")
        return -1

    # conn.commit()

#returns the number of goals a team had in regular season
def get_team_goals(team_name, conn):
    # if whatever the user requested does not exist query should return -1

    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = '''SELECT DISTINCT total_goals_scored FROM Teams WHERE team_name = ?'''
    cur.execute(query, (team_name,))
    output = cur.fetchall()
    conn.commit()

    if len(output) != 0:
        for x in output:
            return (x[0])
    else:
        print("There was nothing to match with your input.")
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
    output = cur.fetchall()
    conn.commit()

    if len(output) != 0:
        for x in output:
            return (x[0])
    else:
        print("There was nothing to match with your input.")
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
    output = cur.fetchall()
    conn.commit()

    if len(output) != 0:
        for x in output:
            return (x[0])
    else:
        print("There was nothing to match with your input.")
        return -1

    # conn.commit()



#returns all players on a team
def get_all_players_from_team(player_team, conn):
    # if whatever the user requested does not exist query should return -1

    # format query from arg

    if conn == None:
        return "No connection found. Please enter the command 'load data' in the terminal."

    cur = conn.cursor()
    query = "SELECT DISTINCT player_name FROM Players WHERE player_team =?"
    cur.execute(query, (player_team,))
    output = cur.fetchall()
    conn.commit()

    if len(output) != 0:
        for x in output:
            return (x[0])
    else:
        print("There was nothing to match with your input.")
        return -1

    # conn.commit()
