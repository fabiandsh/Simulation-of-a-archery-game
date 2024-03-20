import random
from pseudoRandom import PseudoRandom

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
        self.check_win_team()
        players = self.team1.players + self.team2.players
        max_score_player = self.check_win_player(players)
        max_score_player.rounds_won += 1
        print(f'El jugador {max_score_player.name}, gano la ronda')
        self.reset_player()


    def take_additional_throw(self,team):
        """
        Simulates a additional thow by team.

        """
        max_luck_player = max(team.players, key=lambda x: x.luck)
        if max_luck_player.check_extra_throw(): # if is the tree throw
            score = max_luck_player.take_throw()
            team.increase_score(score)
            print(f"El jugador {max_luck_player.name} dio un tiro extra por llegar a los tres tiros ganados")
        score = max_luck_player.take_throw()
        print(f"El jugador {max_luck_player.name} dio un tiro extra por ser el de mayor suerte")
        team.increase_score(score)
        
        
    def take_throws(self, team):
        """
        Simulates a throw by a team's player.

        """
        for player in team.players:
            while player.could_throw():
                score = player.take_throw()
                print(f"El jugador {player.name} tiro con un puntaje de {score}")
                player.increase_round_score(score)
                team.increase_score(score)
            player.add_wear()
        
        self.take_additional_throw(team)



    def check_win_player(self, players):
        """
        Checks if a player has won the round.
        """
        
        max_score_player = max(players, key=lambda x: x.round_score)
        max_score_players = [player for player in players if player.round_score == max_score_player.round_score]
        
        if len(max_score_players) > 1: 
            print(f'Hay un empate, tienen que lanzar')
            players = self.break_tie_players(max_score_players)
            max_score_player= self.check_win_player(players)

        return max_score_player

    def break_tie_players(self,players):
        """
        Break tie players 
        """
        for player in players:
            player.round_score = 0
            player.round_score = player.take_throw()
            print(f'{player.name} lanza y obtine un puntaje de  {player.round_score}')
        return players
                  

        

    def check_win_team(self):
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

    def reset_player(self):
        """
        Resets the lucky for a new round.
        """
        for player in self.team1.players + self.team2.players:
            player.luck = PseudoRandom.getFloatNumberBetween(1,3)
            player.round_score = 0

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
