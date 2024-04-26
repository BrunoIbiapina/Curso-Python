'''Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue
 pedindo até que o usuário informe um valor válido.'''

while True:
    nota = float(input('Digie um número de 0 a 10: '))
    if 0 <= nota <= 10:
        print(f'Sua nota digitada é {nota}')
        break
        
    else:
        print('Valor inválido. A nota deve estar entre 0 e 10')
