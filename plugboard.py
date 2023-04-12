from bidict import bidict


class Plugboard:

    def __init__(self, connections) -> None:
        '''
            Args:
                - settings: A dictionary containing all the plugged pairs of letters in
                    plugboard. For example, if we want the 
                    following connections in plugboard: A-B, X-Y and R-T, 
                    the dictionary will be something like this:

                    connections = {'A': 'B', 'X': 'Y', 'R': 'T'}

                    Then, the attribute 'connections' will be a bidict containing also the inverse mappings.
        '''
        self.connections = bidict(connections)

    def map_letter(self, letter) -> str:
        '''
            This method actually performs the mapping of a letter according to the
            plugboard's settings.
            Args: 
                - letter: the letter to be mapped by the plugboard.
            Returns:
                - new_letter: the resulting letter from the mapping.
        '''
        if letter in self.connections.keys():
            new_letter = self.connections[letter]
        elif letter in self.connections.values():
            new_letter = self.connections.inverse[letter]
        else:
            new_letter = letter

        return new_letter


# Testing the plugboard
if __name__ == '__main__':

    connections = {'A': 'B', 'X': 'Y', 'R': 'T'}
    pb = Plugboard(connections)
    letra = 'Y'

    print(f'Las conexiones son: {pb.connections}')
    print(f'Mapeo: {letra} -> {pb.map_letter(letra)}')
