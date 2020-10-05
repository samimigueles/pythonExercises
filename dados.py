import math
import random


def dados():
    dado1 = int((random.random() *10 ) % 6 + 1)
    dado2 = int((random.random() *10 ) % 6 + 1)
    tirada = print('Tus valores de la tirada son', dado1, dado2, 'y suman', dado1+dado2)
    return tirada

dados()

pregunta = input('Te gustaría volver a tirar? Indica Si o No: ')
while (pregunta == 'Si' or pregunta == 'SI' or pregunta == 'si'):
    dados()
    pregunta = input('Te gustaría volver a tirar?')
else:
    print('Gracias por haber jugado')
