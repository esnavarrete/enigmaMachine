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

    def map_letter(self, letter) -> str:
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

    def rotate(self):
        """
        Just rotates the rotor by one position.
        """
        self.position = (self.position + 1) % len(ALPHABET)
        return


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
