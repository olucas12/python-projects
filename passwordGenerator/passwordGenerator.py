import random
import os

os.system('cls' if os.name=='nt' else 'clear')

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%*()_=+§¹²³£¢¬{[]}\|~^`´.,<>;:?°'

for c in range(16):
    print(f'{chars[random.randint(0, len(chars)-1)]}', end='')

print('\n')