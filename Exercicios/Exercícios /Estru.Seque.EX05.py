'''Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input('Qual valor que você ganha por hora no mês?:'))
horas = float(input('Quantas horas você trabalha por mês?'))
salario = valor_hora * horas
print(f'Você ganha por hora R$ {valor_hora}, então seu salário no final do mês é {salario}')