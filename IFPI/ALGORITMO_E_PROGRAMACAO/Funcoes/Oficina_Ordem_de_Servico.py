# 6 - Oficina: Ordem de Serviço

def calcular_mao_de_obra(horas, valor_hora):
    return horas * valor_hora

def calcular_total_sem_desconto(horas, valor_hora, pecas):
    mao_de_obra = calcular_mao_de_obra(horas, valor_hora)
    total_pecas = sum(pecas)
    return mao_de_obra + total_pecas

def calcular_orcamento_final(horas, valor_hora, pecas, avista):
    total = calcular_total_sem_desconto(horas, valor_hora, pecas)
    if avista:
        total *= 0.92 
    return total

horas = float(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))

entrada_pecas = input("Digite os valores das peças separados por vírgula: ")
pecas = [float(p.strip()) for p in entrada_pecas.split(",")]

forma_pagamento = input("Pagamento à vista? (s/n): ").strip().lower()
avista = forma_pagamento == "s"

total_final = calcular_orcamento_final(horas, valor_hora, pecas, avista)

print("--- ORÇAMENTO FINAL ---")
print(f"Total a pagar: R$ {total_final:.2f}")