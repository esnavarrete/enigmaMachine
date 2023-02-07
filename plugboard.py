class Plugboard:

    def __init__(self, settings) -> None:
        self.settings = settings

    def map_letter(self, letter) -> str:
        if letter in self.settings.keys():
            new_letter = self.settings[letter]
        else:
            new_letter = letter
        return new_letter
