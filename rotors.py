class Rotor:

    def __init__(self, init_position, wiring, notch) -> None:
        self.init_position = init_position
        self.wiring = wiring
        self.notch = notch

    def map_letter(self, letter) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter_index = alphabet.index(letter)
        new_letter = self.wiring[letter_index]
        return new_letter

    def rotate(self, steps):
        print(f'una rotación de {steps}')
        return
