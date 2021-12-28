#Reverses

class Reverses():
    def __init__(bool_value):
        """
        It reverses the given/returned bool.
        If the given bool is a function that returns a bool, it will reverse the bool.
        
        Example:
            Reverses(True): It will return False
            Reverses(False): It will return True
        """
        
        if bool_value == False:
            return True
        elif bool_value == True:
            return False
        
#look... i was bored and i thought this was one of the funny things i ever made