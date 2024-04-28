#Calculadora while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except Exception:
        numeros_validos = None

    if numeros_validos is None:
       print('Um dos números não são vádidos')
       continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Um dos números não são vádidos')
        continue
    
    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue
    
    sair = input('Quer sair? [s]im:').lower().startswith('s')
    if sair is True:
        break   
