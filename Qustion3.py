#Write a program that will load the “football.csv” dataset into a dataframe called
#“foot_ball”. 

 
import pandas as pd

# 3.1 Load the football.csv dataset into a dataframe called "foot_ball"
foot_ball = pd.read_csv("c:/Users/CC/Downloads/dataset - 2020-09-24.csv")

# 3.2 Inspect the dataframe by listing and displaying the last 7 rows
print(foot_ball.tail(7))

# 3.3.1 Access and display the "Nationality" and "Club" columns for all players
print(foot_ball[["Nationality", "Club"]])

# 3.3.2 Access and display the data for the tenth player in the dataset using row index
print(foot_ball.iloc[9])

# 3.3.3 Access and display the "Goals" and "Appearances" for players with index positions 100 to 110
print(foot_ball.loc[100:110, ["Goals", "Appearances"]])

# 3.3.4 Add a new column named "Goals per Appearance" 
foot_ball["Goals per Appearance"] = foot_ball["Goals"] / foot_ball["Appearances"]
#display the first 5 rows of the updated dataset
print(foot_ball.head(5))

# 3.3.5 Select and display a subset of the dataframe containing only the players from "Arsenal" club
arsenal_players = foot_ball[foot_ball["Club"] == "Arsenal"]
print(arsenal_players)

# 3.3.6 Perform a filtering operation to display players who have scored more than 5
high_scorers = foot_ball[foot_ball["Goals"] > 5]
print(high_scorers)
 