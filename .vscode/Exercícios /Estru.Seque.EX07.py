'''Faça um Programa que 
peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro'))
numero3 = float(input('Digite outro um número Real: '))
produto = (2 * numero1) * (numero2 / 2)
soma = (3 * numero1) + numero3
cubo = numero2 ** 3

print(f'O produto do primeiro com a metade do segundo é {produto},'
      f'a soma do triplo do primeiro com o terceiro é {soma} '
      f'\ne a o terceiro elevado ao cubo é {cubo}')