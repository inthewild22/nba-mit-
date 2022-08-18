from game import Game
import random
class Playoffs:

    def __init__(self, east_playoffs, west_playoffs, teams):
        self.east_playoffs = east_playoffs
        self.west_playoffs = west_playoffs
        self.teams = teams


    # creat a function to simulate the playoffs
    def tournament (self):
        all_conferences = [self.east_playoffs, self.west_playoffs]
        # simulate the first round of the playoffs
        final_round = []
        for i in all_conferences:
            win1 = self.sieries(i[0], i[7],i)

            win2 = self.sieries(i[1], i[6],i)

            win3 = self.sieries(i[2], i[5],i)

            win4 = self.sieries(i[3], i[4],i)

            # simulate the second round of the playoffs
            win5 = self.sieries(win1, win4,i)

            win6 = self.sieries(win2, win3,i)

            # sinulate the third round of the playoffs
            win7 = self.sieries(win5, win6,i)

            final_round.append(win7)
        # simulate the final round of the playoffs
        # picking random home court team from the final round
        home_team = random.choice(final_round)
        # removing the home court team from the final round
        final_round.remove(home_team)
        awau_team = final_round[0]

        champions = self.sieries(home_team, awau_team,0)
        return champions
    def sieries(self, team1, team2,confrence):
        conf_id =[]
        if confrence == 0:
            team1_wins = 0
            team2_wins = 0
            home = Game(team1, team2)
            away = Game(team2, team1)
            for i in range(4):
                winner, loser = home.game()
                if winner == team1:
                    team1_wins += 1
                else:
                    team2_wins += 1
            for i in range(3):
                winner, loser = away.game()
                if winner == team1:
                    team1_wins += 1
                else:
                    team2_wins += 1
            if team1_wins > team2_wins:
                return team1
            else:
                return team2
        else:
            for i in confrence:
                conf_id.append(i.team_id)
            team1_wins = 0
            team2_wins = 0



            if conf_id.index(int(team1.team_id)) < conf_id.index(int(team2.team_id)):
                home =  Game(team1, team2)
                away = Game(team2, team1)
                for i in range(4):
                    winner,loser = home.game()
                    if winner == team1:
                        team1_wins += 1
                    else:
                        team2_wins += 1
                for i in range(3):
                    winner,loser = away.game()
                    if winner == team1:
                        team1_wins += 1
                    else:
                        team2_wins += 1
            else:
                home = Game(team2, team1)
                away = Game(team1, team2)
                for i in range(4):
                    winner,loser = home.game()
                    if winner == team1:
                        team1_wins += 1
                    else:
                        team2_wins += 1
                for i in range(3):
                    winner,loser = away.game()
                    if winner == team1:
                        team1_wins += 1
                    else:
                        team2_wins += 1
            if team1_wins > team2_wins:
                return team1
            else:
                return team2