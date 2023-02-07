class Rotor:

    def __init__(self, init_position, wiring, notch) -> None:
        self.init_position = init_position
        self.wiring = wiring
        self.notch = notch

    def rotate(self, steps):
        print(f'una rotación de {steps}')
        return
