peso_libras = float(input("Digite o seu peso em Libras: "))
altura_polegadas = float(input("Digite sua altura em poegadas"))

peso_kg = peso_libras * 0.45
altura_m = altura_polegadas * 0.0254
imc = peso_kg / altura_m ** 2

print(f"Seu peso é {peso_kg}, aluta é {altura_m} e seu Imc é {imc}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.6 <= imc <= 24.9: 
    print("Peso Ideal")
elif 25 <= imc <= 29.9:
    print("Levemente a cima do peso")
elif 30 <= imc <= 34:
    print("Obesidade grau I")
elif 35 <= imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade Mórbida")