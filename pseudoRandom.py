import random

class PseudoRandom(): 
    """
    A class for managing pseudo-random numbers.
    """

    @classmethod
    def getNumberBeteewZeroAndOne(cls):
        """
        Generates a pseudo-random floating point number between 0 and 1.

        Returns:
            float: A pseudo-random number between 0 and 1.
        """
        return random.random()
    
    @classmethod
    def getIntNumberBeetween(cls, sup, inf):
        """
        Generates a pseudo-random integer between the given upper and lower bounds.

        Args:
            sup (int): The upper bound (inclusive) of the range.
            inf (int): The lower bound (inclusive) of the range.

        Returns:
            int: A pseudo-random integer between sup and inf.
        """
        return random.randint(sup, inf)
    
    
    @classmethod
    def getFloatNumberBetween(cls, sup, inf):
        """
        Generates a pseudo-random floating-point number between the given upper and lower bounds.

        Args:
            sup (float): The upper bound (inclusive) of the range.
            inf (float): The lower bound (inclusive) of the range.

        Returns:
            float: A pseudo-random floating-point number between sup and inf.
        """
        return random.uniform(sup, inf)

    @classmethod
    def getIntNumberBeetweenWithNormalDistribution(cls, media, desviacion_estandar):
        """
        Generates a pseudo-random integer from a normal distribution.

        Args:
            media (float): The mean (center) of the distribution.
            desviacion_estandar (float): The standard deviation (spread or width) of the distribution.

        Returns:
            int: A pseudo-random integer from a normal distribution.
        """
        return round(random.normalvariate(media, desviacion_estandar))
