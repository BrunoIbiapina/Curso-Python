peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite seu peso em Metros: "))

imc = peso / altura ** 2
if imc < 18.5:
    print ( " Abaixo do Peso")
elif 18.5 <= imc <= 24.9 :
    print("Peso ideal")
elif 25 <= imc <= 29.9 :
    print("Levemente a cima do peso")
elif 30 <= imc <= 34.9 :
    print("Obesidade grau I")
elif 35 <= imc <= 39.9 :
    print("Obesidade grau II")
else:
    print("Obesidade mórbida")