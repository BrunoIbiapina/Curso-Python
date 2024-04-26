"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#UM MODO DE FAZER O EXERCÍCIO
'''
entrada = input('Digite um número inteiro:')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Ímpar'
if par_impar_texto:
    par_impar_texto = 'Par'
    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')'''

#OUTRO MODO DE FAZER O EXERSÍCIO
entrada = input('Digite um número inteiro: ')
try:
    entrada_int = int(entrada)
    entrada_impar = entrada_int % 2 == 0
    entrada_impar_texto = 'Ímpar'
    if entrada_impar:
        entrada_impar_texto = 'Par'
    print(f'O número {entrada} é {entrada_impar_texto}')
except:
    print('Você não digitou um número Inteiro')