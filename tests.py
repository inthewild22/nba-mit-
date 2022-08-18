
from team import Team
from game import Game


def test_game_and_team():
    print("testing game and team")
    team1 = Team('team1', 'East', 3000, 1)
    team2 = Team('team2', 'East', 1, 2)
    team1_wins = 0
    team2_wins = 0
    game1 = Game(team1, team2)
    for i in range(100):
        winner, loser = game1.game()
        if winner == team1:
            team1_wins += 1
        else:
            team2_wins += 1
    if team1_wins > team2_wins:
        print("pass")
    else:
        print("fail")

test_game_and_team()