from rotors import Rotor
from plugboard import Plugboard
from machine import EnigmaMachine
from settings import REFLECTOR_WIRING, R1_WIRING, R2_WIRING, R3_WIRING, R4_WIRING, R5_WIRING, alphabet

print('*** ENIGMA ENCRYPTION MACHINE ***\n')

# Asking for initial settings
first_rotor = int(input('First rotor?: '))
second_rotor = int(input('Second rotor?: '))
third_rotor = int(input('Third rotor?: '))

init_pos_r1 = int(input('First rotor initial position [0-25]: '))
init_pos_r2 = int(input('Second rotor initial position [0-25]: '))
init_pos_r3 = int(input('Third rotor initial position [0-25]: '))

plugs = input('Plugboard settings (list): ')


# Initializing the machine
plugboard = Plugboard(plugs)
r1 = Rotor(init_pos_r1)
r2 = Rotor(init_pos_r2)
r3 = Rotor(init_pos_r3)

enigma_machine = EnigmaMachine(r1, r2, r3, REFLECTOR_WIRING, plugboard)
