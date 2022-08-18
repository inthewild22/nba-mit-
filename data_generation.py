import csv
import pandas as pd
function i used to generate 2021-2022 elo
# reading the csv file
df = pd.read_csv("teamelo.csv")

for i in range(len(df)):
    # updating the column value/data
    df.loc[i, '2021-2022 elo'] = int(int(df.loc[i, "2020-2021 elo"])*0.75 + 0.25*1500)

    # writing into the file
    df.to_csv("teamelo.csv", index=False)


for a in data[1:]:
    team_instances[int(a[2])] = Team(a[2], a[3], a[0], a[4])

df1 = pd.read_csv("games.csv")

for i in range(len(df1)):
    temp_game = RegularSeason

data = list(csv.reader(open("teamelo.csv")))
data2 = list(csv.reader(open("teams.csv")))
with open("newteamelo.csv","w") as f:
    for i,k in enumerate(data):
        for j in data2:
            if k[2] ==j[5]:
                k.append(j[1])
                csv.writer(f).writerow(k)
gdf = pd.read_csv("games.csv")
gdf2 = gdf.query("SEASON == 2021")
# print(gdf2)