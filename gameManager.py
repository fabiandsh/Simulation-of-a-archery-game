import random
from player import Player
from team import Team
from game import Game


class GameManager:
    """
    Manages the initialization and execution of the game.
    """

    def __init__(self, games):
        """
        Initializes the game manager.
        """
        self.team1 = self.create_team("1")
        self.team2 = self.create_team("2")
        self.game = Game(self.team1, self.team2)
        self.teams_Winners = []
        self.players_with_better_lucky = []
        self.players_with_better_experience = []
        self.count_men = 0
        self.count_women = 0
        self.players_scores = []
        self.game_number = 0

        for _ in range(10):
            self.players_scores.append([])

        for i in range(0, games):
            self.play_game()
            self.save_winner()
            self.save_b_lucky()
            self.save_b_experience()
            self.save_gender_winners()
            self.save_players_scores()
            self.reset_game()

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
        return Team(players, f"Team{group_number}")

    def play_game(self, rounds=10):
        """
        Plays the game for a specified number of rounds.

        Args:
            rounds (int, optional): The number of rounds to play. Defaults to 10.
        """
        for _ in range(rounds):
            self.game.play_round()
            """
            for jugador in game_manager.team1.players:
                jugador.print_info()
            for jugador in game_manager.team2.players:
                jugador.print_info()
            """

    def reset_game(self):
        self.game_number+=1
        print(f'Juego número{self.game_number} terminado')
        self.game.reset_game()

    def save_winner(self): 
        if self.game.teamWinner != None:
            self.teams_Winners.append(f"El ganador fue {self.game.teamWinner.name} con una puntuación de {self.game.teamWinner.score} ")
        else:
             self.teams_Winners.append(f"Fue empate con una puntuación de {self.game.team1.score} ")

    def save_b_lucky(self): 
        players = self.team1.players + self.team2.players
        player_with_better_lucky  = max(players, key=lambda x: x.luck)
        self.players_with_better_lucky.append(f"El jugador con mayor suerte fue {player_with_better_lucky.name}")
        
       
    def save_b_experience(self): 
         players = self.team1.players + self.team2.players
         player_with_better_experience  = max(players, key=lambda x: x.experience)
         self.players_with_better_experience.append(f"El jugador con mayor experiencia fue {player_with_better_experience.name}")

    def save_players_scores(self): 
         players = self.team1.players + self.team2.players
         i = 0
         for player in players:
            self.players_scores[i].append(player.score)
            i+=1
             
         
    def save_gender_winners(self):
        if self.game.teamWinner != None:
            for player in self.game.teamWinner.players:
                if player.gender == "Male":
                    self.count_men+=1
                else: 
                    self.count_women+=1
"""
if __name__ == "__main__":
    # Initialize game manager and play game
    game_manager = GameManager(10)
    
   #para imprimir lista ganadores equipos
    print("Lista ganadores por equipos")
    for team in game_manager.teams_Winners:
        print(team)

    print("Lista jugadores con mayor suerte")
    for player in game_manager.players_with_better_lucky:
        print(player)
    
    print("Lista jugadores con mayor experiencia")
    for player in game_manager.players_with_better_experience:
        print(player)

    print(f"La cantidad de hombres que ganaron fueron : {game_manager.count_men}")
    print(f"La cantidad de mujeres que ganaron fueron : {game_manager.count_women}")
    print("fin de la simulación yei")
"""
