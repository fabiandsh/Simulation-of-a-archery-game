from pseudoRandom import PseudoRandom
class Player:
    """
    Represents a player in the game.
    """

    def __init__(self, name,  experience=10):
        """
        Initializes a player with given attributes.

        Args:
            name (str): The name of the player.
            experience (int, optional): The experience of the player. Defaults to 10.
        """
        self.name = name
        self.gender = gender = "Male" if PseudoRandom.getNumberBeteewZeroAndOne() >0.5 else "Female"
        self.resistance = PseudoRandom.getIntNumberBeetweenWithNormalDistribution(35,10)
        self.actual_resistance = self.resistance
        self.experience = experience
        self.luck = PseudoRandom.getFloatNumberBetween(1,3)
        self.score = 0
        self.round_score = 0
        self.extra_throws = 0
        self.rounds_won = 0
        self.won_bonus = 0


    def assign_target_male(self, random_number):
        """
        Assigns the target for a given random number for men.
        
        Args:
            random_number (float): The random number between 0 and 1.
            
        Returns:
            int: The score for assigned target for men.
        """
        if random_number < 0.20:
            return 10               # Central
        elif random_number < 0.53:  # 0.20 + 0.33 = 0.53
            return 9                # Intermediate
        elif random_number < 0.93:  # 0.20 + 0.33 + 0.40 = 0.93
            return 8                #Outer
        else:
            return 0                #Error

    def assign_target_female(self, random_number):
        """
        Assigns the target for a given random number for women.
        
        Args:
            random_number (float): The random number between 0 and 1.
            
        Returns:
            int: The score for assigned target for women.
        """
        if random_number < 0.30:
            return 10        # Central
        elif random_number < 0.68:  # 0.30 + 0.38 = 0.68
            return 9   # Intermediate
        elif random_number < 0.95:  # 0.30 + 0.38 + 0.27 = 0.95
            return 8          #Outer
        else:
            return 0         #Error
   
    def could_throw(self):
        """
        Check if the player can continue throwing

        Returns:
            boolean: True if the player could throw
        """
        return True if self.actual_resistance >= 5 else False

    def take_throw(self):
        """
        Simulates the player taking a throw, reducing resistance.

        Returns:
            int: Score of the throw
        """
        self.actual_resistance -= 5
        trow = PseudoRandom.getNumberBeteewZeroAndOne()
        return self.assign_target_male(trow) if self.gender == "Male" else self.assign_target_female(trow)


    def check_extra_throw(self):
        """
        Checks if the player can make an extra throw.

        Returns:
            bool: True if an extra throw is allowed, False otherwise.
        """
        if self.extra_throws == 2 :
            self.extra_throws = 0
            return True
        else:
            self.extra_throws += 1
            return False



    def increase_round_score(self, points):
        """
        Increases the player's  round score.

        Args:
            points (int): The points to increase the score by.
        """
        self.round_score += points
        self.score += points
    
    def reset_round_score(self):
        """
        Reset the player's round score
        """
        self.round_score = 0

    def won_round(self):
        """
        Updates player's stats when they win a round.
        """
        self.rounds_won += 1
        self.experience += 3
        if self.rounds_won % 3 == 0: 
            self.won_bonus = 2; 
            print(f"El jugador{self.name} obtuvo bonificación solo se le resta 1 a su resitencia por dos rondas ")



    def add_wear(self):
        """
        Least one or two units, which represent fatigue from the game, or  least 1 if the player is bonused
        """
        if self.won_bonus > 0:
            self.resistance-=1
            print("Solamente se le resta 1")
        else:
            self.resistance = self.resistance - PseudoRandom.getIntNumberBeetween(1,2)



    def print_info(self):
        """
        Prints the information of the player.
        """
        print(f"Player Information: Name: {self.name}, Gender: {self.gender}, Resistance: {self.resistance}, Actual resistence: {self.actual_resistance}, Experience: {self.experience}, Luck: {self.luck}, Score: {self.score}, Round Score : {self.round_score}, Extra Throws: {self.extra_throws}, Rounds Won: {self.rounds_won} ")