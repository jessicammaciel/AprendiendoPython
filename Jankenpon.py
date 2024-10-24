# piedra papel y tijera

from random import randint
from time import sleep #para los segundos antes de jugar
print('{:=^40}'.format(' JUEGO PIEDRA, PAPEL Y TIJERA '))

#array
opcion = ('Piedra', 'Papel', 'Tijera')

comput= randint(0, 2)

print('''[0] PIEDRA
[1] PAPEL
[2] TIJERA''')
jogador = int(input('Elige una opción: '))
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('YA')


print('-=' * 11)
print('Opcion elegida por el ordenador: {}'.format(opcion[comput]))

print('Tu opción: {}'.format(opcion[jogador]))
print('-=' * 11)

if comput == 0: # opcion piedra del ordenador
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('GANASTE!!!!')
    elif jogador == 2:
        print('PERDISTE')
    else:
        print('Opción invalida.')
elif comput == 1: # opcion papel del ordenador
    if jogador == 0:
        print('PERDISTE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('GANASTE!!!!')
    else:
        print('Opción invalida.')
elif comput == 2: # opcion tijera del ordenador
    if jogador == 0:
        print('GANASTE!!!!')
    elif jogador == 1:
        print('PERDISTE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opción invalida.')