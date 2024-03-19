import random

class Game:
    """
    Represents the game instance.
    """

    def __init__(self, team1, team2):
        """
        Initializes the game with two teams.

        Args:
            team1 (Team): The first team.
            team2 (Team): The second team.
        """
        self.team1 = team1
        self.team2 = team2
        self.round_number = 0

    def play_round(self):
        """
        Plays a round of the game.
        """
        self.round_number += 1
        print(f"Round {self.round_number}")

        self.take_throws(self.team1)
        self.take_throws(self.team2)
        self.check_win()

    def take_throws(self, team):
        """
        Simulates a throw by a team's player.

        """
        for player in team.players:
            while player.could_throw():
                score = player.take_throw()
                print(f"El jugador {player.name} tiro con un puntaje de {score}")
                player.increase_score(score)
                team.increase_score(score)
            player.add_wear()
            

    def check_win(self):
        """
        Checks if a team has won the game.
        """
        print("Team 1 Score:", self.team1.score)
        print("Team 2 Score:", self.team2.score)
        if self.round_number == 10:
            if self.team1.score > self.team2.score:
                print("Team 1 Wins!")
            elif self.team2.score > self.team1.score:
                print("Team 2 Wins!")
            else:
                print("It's a tie!")
            #self.reset_game()

    def reset_game(self):
        """
        Resets the game for a new round.
        """
        for player in self.team1.players + self.team2.players:
            player.reset_rounds_won()
            player.resistance = random.randint(25, 45)
            player.score = 0
            player.extra_throws = 0
        self.team1.score = 0
        self.team2.score = 0
        self.round_number = 0
