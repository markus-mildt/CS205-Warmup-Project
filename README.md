# CS205-Warmup-Project

[Trello Board](https://trello.com/b/M300vmgU/cs205-project-al-nb-sh-mm)


Commands: 
"quotes" indicates user input

help - get help with commands  

load data - creates the database and loads the data from the csv  

"player name" location - gets the location of the team that the user-specified player is on  
    SELECT location FROM Players WHERE player_name = ?;

"player name" team - gets the name of the team that a user-specified player is on  
    SELECT team_name FROM Players WHERE player_name = ?;

"Player name" position - gets the position of a user-specified player
    SELECT position FROM Teams WHERE player_name = ?;

Team Name location - gets the location of a user-specified team 
    SELECT location FROM Teams WHERE team_name = ?;
     
Team Name goals - gets the number of goals for a user-specified team  
    SELECT goals FROM Teams WHERE team_name = ?;

"player name" goals - gets the number of goals that a user-specified player got  
    SELECT individual_goals FROM Teams WHERE player_name = ?;

Team Name "location" - gets the team(s) at a user-specified location  
    SELECT team_name FROM Teams WHERE location = ?;

