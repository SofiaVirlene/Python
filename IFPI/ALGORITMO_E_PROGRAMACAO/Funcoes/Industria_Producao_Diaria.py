# 2 - Indústria: Produção Diária

def calcular_producao_total(unidades_por_hora, horas):
    return unidades_por_hora * horas

def calcular_perdas_total(unidades_por_hora, horas, defeituosos, quebrados):
    total_produzido = calcular_producao_total(unidades_por_hora, horas)
    perdas = defeituosos + quebrados
    if perdas > total_produzido:
        print("Erro: perdas maiores que a produção total.")
        return 0
    return perdas

def calcular_producao_liquida(unidades_por_hora, horas, defeituosos, quebrados):
    total_produzido = calcular_producao_total(unidades_por_hora, horas)
    perdas = calcular_perdas_total(unidades_por_hora, horas, defeituosos, quebrados)
    return total_produzido - perdas

unidades_por_hora = float(input("Digite as unidades produzidas por hora: ").strip())
horas = float(input("Digite o número de horas trabalhadas: ").strip())
defeituosos = float(input("Digite a quantidade de unidades defeituosas: ").strip())
quebrados = float(input("Digite a quantidade de unidades quebradas: ").strip())

total = calcular_producao_total(unidades_por_hora, horas)
perdas = calcular_perdas_total(unidades_por_hora, horas, defeituosos, quebrados)
liquida = calcular_producao_liquida(unidades_por_hora, horas, defeituosos, quebrados)

print("--- RESULTADO ---")
print(f"\nProdução total: {total}")
print(f"Perdas totais: {perdas}")
print(f"Produção líquida: {liquida}")