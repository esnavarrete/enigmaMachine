from settings import ALPHABET


class EnigmaMachine:
    def __init__(self, r1, r2, r3, ref, pb) -> None:
        # Rotor instances:
        self.rotor1 = r1
        self.rotor2 = r2
        self.rotor3 = r3
        self.reflector = ref

        # Plugboard instance
        self.plugboard = pb

    def cipher_letter(self, letter):
        """
        Function to cipher a letter via the Enigma Machine. The 
        ciphering process goes through the following steps: 
            1) Plugboard
            2) Rotors: R1 -> R2 -> R3
            3) Reflector (UKW)
            4) Rotors: R3 -> R2 -> R1
            5) Plugboard
            6) Rotation of the corresponding rotors
        """
        print(f'Se entró al cifrado. Input: {letter}')
        # Step 1
        new_letter = self.plugboard.map_letter(letter)

        # Step 2
        new_letter = self.rotor1.map_letter(new_letter)
        new_letter = self.rotor2.map_letter(new_letter)
        new_letter = self.rotor3.map_letter(new_letter)

        # Step 3
        new_letter = self.reflector.map_letter(new_letter)

        # Step 4
        new_letter = self.rotor3.map_letter(new_letter)
        new_letter = self.rotor2.map_letter(new_letter)
        new_letter = self.rotor1.map_letter(new_letter)

        # Step 5
        new_letter = self.plugboard.map_letter(new_letter)

        # Step 6
        notch_position_1 = ALPHABET.index(self.rotor1.notch)
        notch_position_2 = ALPHABET.index(self.rotor2.notch)

        self.rotor1.rotate()
        if self.rotor1.position == notch_position_1:
            self.rotor2.rotate()
        if self.rotor2.position == notch_position_2:
            self.rotor3.rotate()

        return new_letter


# Testing the entire machine
if __name__ == '__main__':
    from settings import ROTOR_WIRINGS, ROTOR_NOTCHES, UKW_WIRINGS
    from rotors import Rotor
    from plugboard import Plugboard

    r1 = Rotor(0, ROTOR_WIRINGS[0], ROTOR_NOTCHES[0])
    r2 = Rotor(0, ROTOR_WIRINGS[1], ROTOR_NOTCHES[1])
    r3 = Rotor(0, ROTOR_WIRINGS[2], ROTOR_NOTCHES[2])
    refl = Rotor(0, UKW_WIRINGS[0], ROTOR_NOTCHES[0])
    pb = Plugboard({'A': 'X'})
    machine = EnigmaMachine(r1, r2, r3, refl, pb)

    letra = 'A'
    print(f'Mapeo Enigma: {letra} -> {machine.cipher_letter(letra)}')
