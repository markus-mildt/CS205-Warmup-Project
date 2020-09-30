# calls help, just a bunch of print statements detailing how to use our program

def help():
      print("Hello! Welcome to our CS205 Warmup Project.  For this projects, we have created"
          " a command-line interface to query data from a database of hockey teams and players.")
      print("")

      print("Here are the commands for players (PLAYERS MUST HAVE QUOTES AROUND NAME):")
      print("Keywords: location, team, position, goals")
      print("\"player-name\" location")
      print("ex: \"Jack Eichel\" location |     returns New York")
      print("")

      print("\"player-name\" team")
      print("ex: \"Jack Eichel\" team     |        returns Buffalo Sabres")
      print("")

      print("\"player-name\" position")
      print("ex: \"Jack Eichel\" position |     returns Center")
      print("")


      print("\"player-name\" goals")
      print("ex: \"Jack Eichel\" goals    |       returns 36")
      print("")


      print("")
      print("Here are the commands for teams (TEAMS NOT IN QUOTES):")
      print("Keywords: team, goals, players")
      print("team \"location\"")
      print("ex: team \"Massachusetts\"   |     returns Boston Bruins")
      print("")

      print("team-name goals")
      print("ex: Buffalo Sabres goals   |      returns 193")
      print("")

      print("team-name players")
      print("ex: Buffalo Sabres players |     returns entire roster of team")
      print("")

      print("Finally, we have a command for loading the data (load data) and quit.")
      print("If you have any questions, please contact our technical support team. Happy querying!")
      print("")