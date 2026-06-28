# Evento: Bilheteria

def calcular_total_ingressos(qtd_inteira, qtd_meia, valor_inteira):
    valor_meia = valor_inteira / 2
    total = (qtd_inteira * valor_inteira) + (qtd_meia * valor_meia)
    return total

def calcular_total_com_taxa(qtd_inteira, qtd_meia, valor_inteira, taxa):
    total = calcular_total_ingressos(qtd_inteira, qtd_meia, valor_inteira)
    total += total * taxa
    return total

def gerar_recibo(nome, qtd_inteira, qtd_meia, valor_inteira, taxa):
    valor_final = calcular_total_com_taxa(qtd_inteira, qtd_meia, valor_inteira, taxa)

    recibo = (f"""
--- RECIBO DE COMPRA ---
Cliente: {nome}
Ingressos Inteira: {qtd_inteira}
Ingressos Meia: {qtd_meia}
Valor final: R$ {valor_final:.2f}
""")
    return recibo

nome = input("Nome do cliente: ")
qtd_inteira = int(input("Quantidade de ingressos inteira: "))
qtd_meia = int(input("Quantidade de ingressos meia: "))
valor_inteira = float(input("Valor do ingresso inteira: "))
taxa = float(input("Taxa administrativa (ex: 0.05 para 5%): "))

print(gerar_recibo(nome, qtd_inteira, qtd_meia, valor_inteira, taxa))