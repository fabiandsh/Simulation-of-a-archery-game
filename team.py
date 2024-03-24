class Team:
    """
    Represents a team in the game.
    """

    def __init__(self, players, name):
        """
        Initializes a team with given players.

        Args:
            players (list): List of Player objects representing the team's players.
        """
        self.name = name
        self.players = players
        self.score = 0

    def increase_score(self, points):
        """
        Increases the team's score.

        Args:
            points (int): The points to increase the score by.
        """
        self.score += points
