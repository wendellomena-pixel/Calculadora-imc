# Calculadora de IMC

print("=== CALCULADORA DE IMC ===")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

print(f"\nOlá," {nome})
print(f"Seu IMC é:" {round imc, 2})