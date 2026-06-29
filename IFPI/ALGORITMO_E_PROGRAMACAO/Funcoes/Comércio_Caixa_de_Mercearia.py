# 1 - Comércio: Caixa de Mercearia

def calcular_total(itens):
    return sum(itens)

def calcular_total_com_desconto(itens, cupom):
    total = calcular_total(itens)
    cupom = cupom.strip().upper()
    if cupom == "DESC10":
        percentual = 0.10
    elif cupom == "DESC5":
        percentual = 0.05
    else:
        percentual = 0
    return total - (total * percentual)

def calcular_troco_final(itens, cupom, pago):
    total_final = calcular_total_com_desconto(itens, cupom)
    if pago > total_final:
        troco = pago - total_final
        print(f"Total final: R$ {total_final:.2f}")
        print(f"Troco: R$ {troco:.2f}")
    elif pago == total_final:
        print(f"Total final: R$ {total_final:.2f}")
        print("Pagamento exato. Sem troco.")
    else:
        print(f"Total final: R$ {total_final:.2f}")
        print("Valor insuficiente.")

entrada_itens = input("Digite os preços separados por vírgula: ")
itens = [float(preco.strip()) for preco in entrada_itens.split(",")]
cupom = input("Digite o cupom (DESC10, DESC5 ou outro): ")
pago = float(input("Digite o valor pago: "))
calcular_troco_final(itens, cupom, pago)