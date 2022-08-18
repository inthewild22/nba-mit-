class Team():
    all_teams = {}
    def __init__(self,team_name,conference,elo,team_id):
        self.team_name = team_name
        self.conference = conference
        self.elo = elo
        self.team_id = team_id
        self.__class__.all_teams[self.team_id] = self
    def __str__(self):
        return f"{self.team_name},{self.elo}"
    def __eq__(self, other):
        return self.team_id == other.team_id
    def __del__(self):
        del self


