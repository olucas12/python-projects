"""
Random password generator
"""

import random
import os

os.system('cls' if os.name=='nt' else 'clear')

characters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*./\|+=-_'
password = ''

for i in range(12):
    char = characters[random.randint(0, len(characters)-1)]
    if char.isalpha():
        percent = random.randint(0, 100)
        if percent <= 50:
            password+=char
        elif percent > 50:
            password+=char.upper()
    else:
        password+=char

print(f'{password}\n')