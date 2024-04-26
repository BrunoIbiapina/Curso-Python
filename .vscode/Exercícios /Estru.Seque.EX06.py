'''Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).'''

graus_fahrenheit = float(input('Quantos graus Fahrenheite deseja convercer para C? '))
conversao = 5 * ((graus_fahrenheit-32) /9)
print(f'{graus_fahrenheit} graus Fahrenheite convertido para Celsius é: {conversao}')