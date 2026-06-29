# 8 - Logística

def calcular_valor_peso(peso_kg):
    return peso_kg * 2

def calcular_valor_base_frete(peso_kg, km):
    valor_peso = calcular_valor_peso(peso_kg)
    valor_km = km * 0.50
    return valor_peso + valor_km

def calcular_frete_total(peso_kg, km, risco):
    total = calcular_valor_base_frete(peso_kg, km)
    if risco:
        total *= 1.15
    return total

peso = float(input("Digite o peso (kg): "))
km = float(input("Digite a distância (km): "))
risco_input = input("Carga de risco? (s/n): ").strip().lower()
risco = risco_input == "s"

valor_total = calcular_frete_total(peso, km, risco)

print("--- FRETE TOTAL ---")
print(f"Valor final: R$ {valor_total:.2f}")