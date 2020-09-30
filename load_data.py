import sqlite3
import csv

def create_table():
    #create a connection to the database
    conn = sqlite3.connect('NHL.db')
    cur = conn.cursor()

    # Create TEAMS Table
    cur.execute('''CREATE TABLE IF NOT EXISTS TEAMS 
            ([generated_id] INTEGER PRIMARY KEY,[team_name] text,[location] text,[total_goals_scored] integer)''')

    # Create PLAYERS Table
    cur.execute('''CREATE TABLE IF NOT EXISTS PLAYERS 
            ([generated_id] INTEGER PRIMARY KEY,[player_name] text,[player_team] text,[current_position] text,
            [individual_goals_scored] integer)''')

    conn.commit()
    return conn


def load_data():
    create_table()
    conn = sqlite3.connect('NHL.db')
    cur = conn.cursor()

    # open csv and read it
    skaters_file = open("skaters_nhl.csv")
    skaters_rows = csv.reader(skaters_file)

    # insert data into table
    cur.executemany('''INSERT INTO PLAYERS (player_name,player_team,current_position,individual_goals_scored) 
    VALUES (?,?,?,?)''', skaters_rows)
    skaters_file.close()

    #open csv and read it
    teams_file = open("teams_nhl.csv")
    teams_rows = csv.reader(teams_file)

    #insert data into table
    cur.executemany('''INSERT INTO TEAMS (team_name,location,total_goals_scored) 
        VALUES (?,?,?)''', teams_rows)

    #close the file
    teams_file.close()

    #save changes
    conn.commit()
    return conn

