'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

import math
valor_circulo = float(input('Digite o raio de desejado para o circulo: '))
area = math.pi * (valor_circulo ** 2)
print(f'O valor do raio do de um circulo é {valor_circulo} e sua área tem o valor de {area:.1f}')
