import random
from team import Team

class Game:

    def __init__(self, h_team, a_tean):
        self.h_team = h_team
        self.a_team = a_tean

    def game(self):
        # adding home court adventege
        h_team_adv = self.h_team.elo+5
        # calulate odds of winning for home team
        pr_h = 1 / (1 + 10 ** (((self.a_team.elo - h_team_adv)) / 400))
        pr_a = 1-pr_h

        winner =  random.choices([self.h_team ,self.a_team],[pr_h,pr_a])

        if winner[0] is self.h_team:
            # updating the elo and returning the winner and loser
            self.h_team.elo = self.h_team.elo+20*(1-pr_h)
            self.a_team.elo = self.a_team.elo+20*(0-pr_a)
            return self.h_team, self.a_team
        self.h_team.elo = self.h_team.elo + (20 * (0 - pr_h))
        self.a_team.elo = self.a_team.elo + (20 * (1 - pr_a))
        return  self.a_team, self.h_team



