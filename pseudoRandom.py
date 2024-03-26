import random
from readFiles import Manage_psuedo_random_numbers

class PseudoRandom(): 
    """
    A class for managing pseudo-random numbers.
    """
    rf = Manage_psuedo_random_numbers()

    @classmethod
    def getNumberBeteewZeroAndOne(self):
        """
        Generates a pseudo-random floating point number between 0 and 1.

        Returns:
            float: A pseudo-random number between 0 and 1.
        """
        return self.rf.get_ri_number_uniform()
    
    @classmethod
    def getIntNumberBeetween(self, sup, inf):
        """
        Generates a pseudo-random integer between the given upper and lower bounds.

        Args:
            sup (int): The upper bound (inclusive) of the range.
            inf (int): The lower bound (inclusive) of the range.

        Returns:
            int: A pseudo-random integer between sup and inf.
        """
        return self.rf.get_int_between_uniform(sup, inf)
    
    
    @classmethod
    def getFloatNumberBetween(self, sup, inf):
        """
        Generates a pseudo-random floating-point number between the given upper and lower bounds.

        Args:
            sup (float): The upper bound (inclusive) of the range.
            inf (float): The lower bound (inclusive) of the range.

        Returns:
            float: A pseudo-random floating-point number between sup and inf.
        """
        return self.rf.get_float_between_uniform(sup, inf)

    @classmethod
    def getIntNumberBeetweenWithNormalDistribution(self, media, desviacion_estandar):
        """
        Generates a pseudo-random integer from a normal distribution.

        Args:
            media (float): The mean (center) of the distribution.
            desviacion_estandar (float): The standard deviation (spread or width) of the distribution.

        Returns:
            int: A pseudo-random integer from a normal distribution.
        """
        return self.rf.get_int_between_normal()
