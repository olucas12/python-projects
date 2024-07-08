"""
Create usernames using user name
"""

import os
import unidecode  # Necessita instalação (pip install unidecode)
import random

os.system('cls' if os.name=='nt' else 'clear')

nome = input('Digite o nome: ')
nome = unidecode.unidecode(nome)  # Retira os acentos

corte = nome.lower().split()

primeiroNome = corte[0]

sobrenome = corte[len(corte)-1]
posicaoSobrenome = len(corte)-1

meio = ''
limit = 0

for nome in corte[1:posicaoSobrenome]:
    if len(nome) > 3 and limit <3:
        for letra in nome:
            meio += letra
            limit+=1
            break

numero = random.randint(0,999)

print(f'\n{primeiroNome}.{meio}{sobrenome}{numero:02}\n')
