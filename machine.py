class EnigmaMachine:
    def __init__(self, r1, r2, r3, ref, pb) -> None:
        self.rotor1 = r1
        self.rotor2 = r2
        self.rotor3 = r3
        self.reflector = ref
        self.plugboard = pb

    def cipher_letter(self, letter):
        print(f'Se entró al cifrado, {letter}')
        return letter
