import pickle
from regular_season import RegularSeason
from playoffs import Playoffs

# overall - great work! 
# you have a lot of logic that works well.
# for the course future puposes - think about the data you can save in db. 
# for example: 
# save the games in a table (this way you can see history of the games). etc.
# 
# pay attention to my comments



picklefile = open('team_instances', 'rb')
team_instances = pickle.load(picklefile)
picklefile.close()

for team in team_instances.values():
    team.elo = int(float(team.elo))
    team.team_id = int(team.team_id)




win_tracker = {}
clinched_playoffs = {}

# since you program is a bit complicated - it would help a bit of comments/documentation 
while True:
    one = RegularSeason(team_instances)
    for team in team_instances.values():
        win_tracker[team.team_name] = {'wins': 0}
        clinched_playoffs[team.team_name] = {'cinched': 0}
    user = input("please enter the amount of seasons you want to simulate:\npress e to exit\n")
    if user.isdigit():
        for reps in range(int(user)):
            east_playoffs, west_playoffs = one.simulate_season()
            for team in clinched_playoffs:
                for east in east_playoffs:
                    if east.team_name == team:
                        clinched_playoffs[team]['cinched'] += 1
                for west in west_playoffs:
                    if west.team_name == team:
                        clinched_playoffs[team]['cinched'] += 1
            two  = Playoffs(east_playoffs, west_playoffs, team_instances)
            champion = two.tournament()
            # count the number of wins for each team
            for team in win_tracker:
                if team == champion.team_name:
                    win_tracker[team]['wins'] += 1
        # delete all teams instances
            for team in team_instances.values():
                del team

            # you already have this code above - put it in a function.
            picklefile = open('team_instances', 'rb')
            team_instances = pickle.load(picklefile)
            picklefile.close()
            for team in team_instances.values():
                team.elo = int(float(team.elo))
                team.team_id = int(team.team_id)


        for team in win_tracker:
            print(f"{team} have {win_tracker[team]['wins'] / int(user)} chanse of winning")
        for team in clinched_playoffs:
            print(f"{team} have {clinched_playoffs[team]['cinched']/int(user)} chanse of clinching the playoffs")
        # in the end when i run it i get very liitle feedback on the screen
        # only the chance of clinching the playoffs and winning.
        # i would like to see results. who won . maybe print it nicely :) or display in html now that we progress

    else:
        if user == 'e':
            break
        print("please enter a valid number")





