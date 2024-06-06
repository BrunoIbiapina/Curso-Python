peso = float(input("Digite seu peso em gramas: "))
altura = float(input("Digite sua altura em centímetros"))

peso_kg = peso / 1000
altura_m = altura / 100
imc = peso_kg / altura_m ** 2

print(f"Seu peso é:  {peso_kg} e sua altura é {altura_m}, então seu imc é {imc} ")