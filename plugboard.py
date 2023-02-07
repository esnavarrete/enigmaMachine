class Plugboard:

    def __init__(self, settings) -> None:
        '''
            Args:
                - settings: A dictionary containing all the plugged pairs of letters in
                    plugboard. Dict keys are the initial letters and dict values are the 
                    corresponding mapped letter. For example, if we want the 
                    following connections in plugboard: A-B, X-Y and R-T, 
                    the dictionary will look like this:

                    settings = {'A': 'B', 'X': 'Y', 'R': 'T'}
        '''
        self.settings = settings

    def map_letter(self, letter) -> str:
        '''
            This method actually performs the mapping of a letter according to the
            plugboard's settings.
            Args: 
                - letter: the letter to be mapped by the plugboard.
            Returns:
                - new_letter: the resulting letter from the mapping.
        '''
        if letter in self.settings.keys():
            new_letter = self.settings[letter]
        else:
            new_letter = letter

        return new_letter
