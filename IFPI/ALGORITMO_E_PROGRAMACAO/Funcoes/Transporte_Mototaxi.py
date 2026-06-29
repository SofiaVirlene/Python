# 5 - Transporte: Mototáxi

def calcular_valor_km(distancia, preco_km):
    return distancia * preco_km

def calcular_valor_com_adicional(distancia, preco_km, noturno):
    valor = calcular_valor_km(distancia, preco_km)
    if noturno:
        valor += valor * 0.20 
    return valor

def calcular_total_corrida(distancia, preco_km, noturno, taxa_fixa):
    valor_corrida = calcular_valor_com_adicional(distancia, preco_km, noturno)
    return valor_corrida + taxa_fixa

distancia = float(input("Digite a distância (km): "))
preco_km = float(input("Digite o preço por km: "))
periodo = input("É corrida noturna? (s/n): ").strip().lower()
taxa_fixa = float(input("Digite a taxa fixa: "))

noturno = periodo == "s"

total = calcular_total_corrida(distancia, preco_km, noturno, taxa_fixa)

print("--- RESULTADO ---")
print(f"Valor total da corrida: R$ {total:.2f}")