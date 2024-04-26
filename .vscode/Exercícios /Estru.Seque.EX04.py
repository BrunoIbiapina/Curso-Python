'''Faça um Programa que calcule a área de um quadrado,
 em seguida mostre o dobro desta área para o usuário.'''

import math
area = float(input('Digite a área do quadrato: '))
dobro_area = math.pow(area,2)
print(f'O dobro da área do quadrado é {dobro_area:.1f} ')