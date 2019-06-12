class PlayGame:
    """Plays the dice game Pig with two players"""
    def __init__(self):
        self.player_one = Player(turn=True)
        self.player_two = self.get_opponent()
        self.scoreboard = Scoreboard(self.player_one, self.player_two)
        self.start_game()
    
    def get_opponent(self):
        number_of_players = None
        while True:
            number_of_players = input("How many players? ")
            try:
                if int(number_of_players) == 2:
                    return Player()
                elif int(number_of_players) == 1:
                    print("Computer opponent coming soon!")
                else:
                    print("Players more than 2 not supported yet.")
            except:
                print("Invalid entry, try again.")
    
    def start_game(self):
        print("Game Started")

class Scoreboard:
    """Tracks scores for the current turn, game, and multiple games"""
    def __init__(self, player_one, player_two, best_of=1):
        self.player_one = player_one
        self.player_two = player_two
        self.best_of = best_of

class Player:
    """Makes a player class"""
    def __init__(self, turn=False):
        self.score = 0
        self.turn = turn

PlayGame()