from typing_extensions import TypeAlias, List

Team: TypeAlias = list["Football"]

class Football: 
    def __init__(self, player: str):
        self.player = player

    @staticmethod
    def create_team(team_player: List[str]) -> Team:
        return [Football(player) for player in team_player]


# Creating individual players
player1 = Football("PLayer1")
player2 = Football("Player2")

Machester_United = Football.create_team(["Hendrick", "Adam"])
print(Machester_United[0].player)
print(Machester_United[1].player)