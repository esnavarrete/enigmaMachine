from rotors import Rotor
from plugboard import Plugboard
from machine import EnigmaMachine
from settings import *

print('*** ENIGMA ENCRYPTION MACHINE ***\n')

# Asking for initial settings
first_rotor = int(input('First rotor? [0-4]: '))
second_rotor = int(input('Second rotor? [0-4]: '))
third_rotor = int(input('Third rotor? [0-4]: '))

init_pos_r1 = int(input('\nFirst rotor initial position [0-25]: '))
init_pos_r2 = int(input('Second rotor initial position [0-25]: '))
init_pos_r3 = int(input('Third rotor initial position [0-25]: '))

ukw = int(input('\nReflector? [0 (A), 1 (B), 2(C)]: '))
plugged_pairs = {pair[0]: pair[1]
                 for pair in input("Enter the plugged pairs in Plugboard: ").split()}


# Initializing the machine
plugboard = Plugboard(plugged_pairs)
r1 = Rotor(init_pos_r1, ROTOR_WIRINGS[first_rotor], ROTOR_NOTCHES[first_rotor])
r2 = Rotor(
    init_pos_r2, ROTOR_WIRINGS[second_rotor], ROTOR_NOTCHES[second_rotor])
r3 = Rotor(init_pos_r3, ROTOR_WIRINGS[third_rotor], ROTOR_NOTCHES[third_rotor])

enigma_machine = EnigmaMachine(r1, r2, r3, UKW_WIRINGS[ukw], plugboard)

# Ciphering
# original_msg = str(input('\nEnter your message: ')).upper()
# encrypted_msg = ''

# for letter in original_msg:
#     new_letter = enigma_machine.cipher_letter(letter)
#     encrypted_msg = encrypted_msg + new_letter

# print(f'Original text: {original_msg}')
# print(f'Encrypted text: {encrypted_msg}')


# Cifrando una letra
letra = input('Igrese letra: ').upper()
letra = plugboard.map_letter(letra)
