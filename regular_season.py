from team import Team
import pandas as pd
from game import Game
class RegularSeason:

    def __init__(self,teams):
        self.teams = teams
        self.records = {}
        for team in teams.values():
            self.records[team.team_id] = {'wins':0,'losses':0}

    # this is a  long function. consider breaking it.
    def simulate_season(self):
        with open("2021_regular_season.csv", 'r') as f:
            df = pd.read_csv(f)
        for i in range(len(df)):
            home_team = df.loc[i, "HOME_TEAM_ID"]
            visitor_team = df.loc[i, "VISITOR_TEAM_ID"]
            game_id = df.loc[i, "GAME_ID"]
            game = Game(self.teams[str(home_team)],self.teams[str(visitor_team)])

            winner, loser = game.game()

#             updating the team record
            self.records[winner.team_id]['wins'] += 1
            self.records[loser.team_id]['losses'] += 1
#         seprating the records by conference
        east_records = {}
        west_records = {}
        for i in self.records:
            if self.teams[str(i)].conference == 'East':
                east_records[i] = self.records[i]

            else:
                west_records[i] = self.records[i]

        east_records = sorted(east_records.items(), key=lambda x: x[1]['wins'], reverse=True)
        west_records = sorted(west_records.items(), key=lambda x: x[1]['wins'], reverse=True)
#         play in tournament
#         7nth place vs 8th place
        all_records = [east_records, west_records]
        playin_winners = []
        for i in all_records:
            game = Game(self.teams[str(i[6][0])] , self.teams[str(i[7][0])])
            sevnth_seed, loser = game.game()
            game = Game(self.teams[str(i[8][0])], self.teams[str(i[9][0])])
            winner, dq = game.game()
    #       loser vs winner
            game = Game(self.teams[str(loser.team_id)], self.teams[str(winner.team_id)])
            eighth_seed, dq = game.game()
            playin_winners.append(sevnth_seed)
            playin_winners.append(eighth_seed)
        east_playoffs=[]
        west_playoffs=[]
        for i in range(6):
            east_playoffs.append(self.teams[str(east_records[i][0])])
        east_playoffs.append(playin_winners[0])
        east_playoffs.append(playin_winners[1])
        for i in range(6):
            west_playoffs.append(self.teams[str(west_records[i][0])])
        west_playoffs.append(playin_winners[2])
        west_playoffs.append(playin_winners[3])

        return east_playoffs, west_playoffs