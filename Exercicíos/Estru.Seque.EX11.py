'''Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas 
e o preço total.'''

import math
#definindo as contantes
cobertura_por_litro = 3 #metros quadrados
capacidade_lata = 18 #litros
preco_lata = 80.00 #reais

#Solicitando area a ser pintada 
area = float(input('Qual tamanho da área que deseja pintar, em metros: '))

#calculadndo a quantidade de litros necessários
litros_necessarios = area / cobertura_por_litro

#calcuando latas necessarias
latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)

#calculando preço total
preco_total = latas_necessarias * preco_lata

print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")