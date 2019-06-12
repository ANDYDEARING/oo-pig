SCORE_TO_WIN = 100

class PlayGame:
    """Plays the dice game Pig with two players"""
    def __init__(self):
        self.player_one = Player()
        self.player_two = self.get_opponent()
        self.scoreboard = Scoreboard(self.player_one, self.player_two)
        self.play_game()
    
    def get_opponent(self):
        number_of_players = None
        while True:
            number_of_players = input("How many players? ")
            try:
                if int(number_of_players) == 2:
                    print("Player 2")
                    return Player()
                elif int(number_of_players) == 1:
                    print("Computer opponent coming soon!")
                else:
                    print("Players more than 2 not supported yet.")
            except:
                print("Invalid entry, try again.")
    
    def play_game(self):
        game_over = False
        player_list = [self.player_one, self.player_two]
        first_players_turn = True
        while not game_over:
            self.scoreboard.display()
            if first_players_turn:
                print("Player 1")
                game_over = self.player_one.take_turn()
            else:
                print("Player 2")
                game_over = self.player_two.take_turn()
            first_players_turn = not first_players_turn
        print(f"p1:{self.player_one.score}")
        print(f"p2:{self.player_two.score}")
            
        

class Scoreboard:
    """Tracks scores for the current turn, game, and multiple games"""
    def __init__(self, player_one, player_two, best_of=1):
        self.player_one = player_one
        self.player_two = player_two
        self.best_of = best_of
    
    def display(self):
        print(f"""
            {self.player_one.name}: {self.player_one.score}       {self.player_two.name}: {self.player_two.score}
        """)


class Player:
    """Makes a player class"""
    def __init__(self):
        self.score = 0
        self.winner = False
        self.name = "default"
        valid_input = False
        while not valid_input:
            self.name = input("What's your name? ")
            if len(self.name) < 10:
                valid_input = True
            else:
                print("Only names up to 10 characters are supported")

    def take_turn(self):
        self.score += int(input("Put in a score: "))
        if self.score >= SCORE_TO_WIN:
            print(f"{self.name} wins!")
            self.winner = True
        return self.winner

PlayGame()