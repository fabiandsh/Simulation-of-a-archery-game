import random
from player import Player
from team import Team
from game import Game

class GameManager:
    """
    Manages the initialization and execution of the game.
    """

    def __init__(self):
        """
        Initializes the game manager.
        """
        self.team1 = self.create_team("1")
        self.team2 = self.create_team("2")
        self.game = Game(self.team1, self.team2)

    def create_team(self, group_number):
        """
        Creates a team with 5 players.

        Args:
            name (str): The name of the team.

        Returns:
            Team: The created team.
        """
        players = []
        for i in range(1, 6):
            name = f"J{i}G{group_number}"  
            players.append(Player(name))
        return Team(players)

    def play_game(self, rounds=10):
        """
        Plays the game for a specified number of rounds.

        Args:
            rounds (int, optional): The number of rounds to play. Defaults to 10.
        """
        for _ in range(rounds):
            self.game.play_round()
            for jugador in game_manager.team1.players:
                jugador.print_info()
            for jugador in game_manager.team2.players:
                jugador.print_info()




if __name__ == "__main__":
    # Initialize game manager
    game_manager = GameManager()
    for jugador in game_manager.team1.players:
            jugador.print_info()
            print("--------------------")
    for jugador in game_manager.team2.players:
            jugador.print_info()
            print("--------------------")

    # Play the game
    game_manager.play_game()

