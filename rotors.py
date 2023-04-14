from settings import ALPHABET


class Rotor:

    def __init__(self, init_position, wiring, notch) -> None:
        """
        Args:
            -init_position: Initial position of the rotor [0-25].
            -wiring: String of letters representing the mapping of  
                     the rotor wrt the normal alphabet.
            -notch: letter where the rotor would make a second 
                    rotor placed next to it to rotate as well. 
        """
        self.position = init_position
        self.wiring = wiring
        self.notch = notch

    def map_forward(self, letter) -> str:
        """
        This function maps a letter through the rotor according to
        its wiring configuration

        Args:
            -letter: letter to be mapped by the rotor.
        Returns:
            -new_letter: mapped letter
        """
        letter_position = ALPHABET.index(letter)
        new_letter = self.wiring[(
            letter_position + self.position) % len(ALPHABET)]
        return new_letter

    def map_backward(self, letter) -> str:
        letter_position = ALPHABET.index(letter)
        # (self.wiring.index(ALPHABET[(letter_position + self.position) % len(ALPHABET)]) - self.position) % len(ALPHABET)

        new_letter = ALPHABET[(self.wiring.index(ALPHABET[(
            letter_position + self.position) % len(ALPHABET)]) - self.position) % len(ALPHABET)]
        # letter_position = (self.wiring.index(letter) - self.position) % len(ALPHABET)
        # new_letter = ALPHABET[letter_position]
        return new_letter

    def rotate(self) -> None:
        """
        Just rotates the rotor by one position. It takes into 
        account when the position exceeds the value 25.
        """
        self.position = (self.position + 1) % len(ALPHABET)
        return


class UKW:
    def __init__(self, wiring) -> None:
        self.wiring = wiring

    def reflect(self, letter) -> str:
        letter_position = ALPHABET.index(letter)
        new_letter = self.wiring[letter_position]
        return new_letter


# Testing if the class works
if __name__ == '__main__':

    from settings import ROTOR_WIRINGS, ROTOR_NOTCHES
    letra = 'Z'
    rotor = Rotor(0, ROTOR_WIRINGS[0], ROTOR_NOTCHES[0])

    print(f'Posición inicial: {rotor.position}')
    print(f'Cableado del rotor: {rotor.wiring}')
    print(f'Muesca de cambio: {rotor.notch}')

    print(f'\nPrimer mapeo: {letra} -> {rotor.map_letter(letra)}')
    print(f'Rotando un sólo paso el rotor...')
    rotor.rotate()
    print(f'Segundo mapeo: {letra} -> {rotor.map_letter(letra)}')
