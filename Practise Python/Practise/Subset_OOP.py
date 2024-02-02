class Game():
    game_activated = False

class Play(Game):
    def __init__(self, game_type, player_id):
        self.game_type = game_type
        self.player_id = player_id
        

game = Play("Valorant", 21031117)
print(game.__dict__)
print(type(game).__dict__)
print(game.game_activated)





