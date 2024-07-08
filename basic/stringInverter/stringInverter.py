import os

os.system('cls')

msg = input('Digite uma frase: ')
# msg = 'Socorram me subi no onibus em Marrocos'

x = len(msg)-1

for n in msg:
  print(f'{msg[x]}', end='')
  x-=1
