from settings import ALPHABET


class Rotor:

    def __init__(self, init_position, wiring, notch) -> None:
        self.position = init_position
        self.wiring = wiring
        self.notch = notch

    def map_letter(self, letter) -> str:
        letter_position = ALPHABET.index(letter)
        new_letter = self.wiring[(
            letter_position + self.position) % len(ALPHABET)]
        return new_letter

    def rotate(self):
        self.position = (self.position + 1) % len(ALPHABET)
        return
