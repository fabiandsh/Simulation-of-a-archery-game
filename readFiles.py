import random
import os

class Manage_psuedo_random_numbers():
    
    """
    a class for providing pseudo-random numbers 
    """

    """
    Variables used to store the data of the files (names and values)
    """
    name_normal_file = './files/normal.csv'
    name_normal_ni_file = './files/normal_ni.csv'
    name_uniform_file = './files/uniform'
    normal_data = []
    normal_ni_data = []
    uniform_data = []
    countList=0
    
    def __init__(self):
        """
        Constructor of the class where the data is loaded from the files
        """
        self.fill_normal_list()
        self.fill_normal_ni_list()
        self.fill_uniform_list()
        
        
    @staticmethod
    def is_float(element):
        """
        
        Determinates wheter a string is a float number or not
        Args:
            element (string): number to be evaluated

        Returns:
            boolean: wheter the element is a float number or not 
        """
        try:
            float_value = float(element)
            return isinstance(float_value, float) and len(str(float_value).split('.')[1]) > 5
        except ValueError:
            return False
    
    @classmethod
    def read_file(self, name_file):
        """
        Reads the data from a file and returns a list with the float numbers.
        Shuffle the list to get a random order of the numbers

        Args:
            name_file (string): name of the file to be read

        Returns:
            list: list with the float numbers
        """
        filter_data = []
        data = []
        with open(name_file, 'r') as file:
            for row in file:
                data += row.strip().split(';')
        filter_data = list(filter(self.is_float, data))
        random.shuffle(filter_data)
        return filter_data 
    
    
    
    @classmethod
    def fill_normal_list(self):
        """
        Fills the list with the normal data
        """
        self.normal_data = self.read_file(self.name_normal_file)
    
    @classmethod
    def fill_normal_ni_list(self):
        """
        Fills the list with the normal ni data
        """
        self.normal_ni_data = self.read_file(self.name_normal_ni_file)
        
    @classmethod
    def fill_uniform_list(self):
        """
        Fills the list with the uniform data
        """
        self.uniform_data = self.read_file(f'{self.name_uniform_file}{self.countList}.csv')
     
    @classmethod    
    def get_ri_number_uniform(self):
        """
        Gets a number from the uniform data list

        Returns:
            float: a number from the uniform data list
        """
        if (len(self.uniform_data)== 0):
            self.countList+=1
            self.fill_uniform_list()
        return float(self.uniform_data.pop(0))
    
    @classmethod    
    def get_ri_number_normal(self):
        """
        Gets a number from the normal data list

        Returns:
            float: a number from the normal data list
        """
        return float(self.normal_data.pop(0))
    
    @classmethod 
    def get_int_between_uniform(self, sup, inf):
        """
        Generates a pseudo-random integer between the given upper and lower bounds.

        Args:
            sup (int): superior limit
            inf (int): inferior limit

        Returns:
            int: A pseudo-random integer between sup and inf. 
        """
        return int(inf + (self.get_ri_number_uniform() * (sup - inf)))
    
    @classmethod 
    def get_float_between_uniform(self, sup, inf):
        """
        Generates A pseudo-random floating-point number between the given upper and lower bounds.

        Args:
            sup (int): superior limit
            inf (int): inferior limit

        Returns:
            float: A pseudo-random floating-point number between sup and inf. 
        """
        return float(inf + (self.get_ri_number_uniform() * (sup - inf)))
    
    @classmethod
    def get_int_between_normal(self):
        """
        Generates a pseudo-random integer from a normal distribution.

        Returns:
            int: A pseudo-random integer from a normal distribution.
        """
        return int(float(self.normal_ni_data.pop(0)))
        
