#Calculadora while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except ValueError:
        print('Um dos números não é válido.')
        continue

    if operador not in '+-*/':
        print('Operador inválido.')
        continue

    if operador == '/' and num_2_float == 0:
        print('Não é possível dividir por zero.')
        continue

    print('Realizando sua conta')

    if operador == '+':
       print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui')
    
    sair = input('Quer sair? [s]im:').lower().startswith('s')
    if sair:
        break
