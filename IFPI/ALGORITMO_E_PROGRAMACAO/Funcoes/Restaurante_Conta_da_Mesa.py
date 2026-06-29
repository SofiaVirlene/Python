#3 - Restaurante: Conta da Mesa

def calcular_subtotal(itens):
    return sum(itens)

def aplicar_taxa(valor, taxa_percentual=10):
    taxa_decimal = taxa_percentual / 100
    return valor + (valor * taxa_decimal)

def calcular_total_com_taxa(itens, taxa_percentual=10):
    subtotal = calcular_subtotal(itens)
    return aplicar_taxa(subtotal, taxa_percentual)

def calcular_valor_por_pessoa(itens, pessoas, taxa_percentual=10):
    if pessoas <= 0:
        print("Erro: número de pessoas deve ser maior que zero.")
        return 0

    total = calcular_total_com_taxa(itens, taxa_percentual)
    return total / pessoas

entrada_itens = input("Digite os valores consumidos separados por vírgula: ")
itens = [float(preco.strip()) for preco in entrada_itens.split(",")]

pessoas = int(input("Digite o número de pessoas: ").strip())

taxa_input = input("Digite a taxa de serviço (%) ou pressione Enter para 10%: ").strip()

if taxa_input == "":
    taxa = 10
else:
    taxa = float(taxa_input)

subtotal = calcular_subtotal(itens)
total = calcular_total_com_taxa(itens, taxa)
valor_por_pessoa = calcular_valor_por_pessoa(itens, pessoas, taxa)

print("--- RESULTADO ---")
print(f"\nSubtotal: R$ {subtotal:.2f}")
print(f"Total com taxa: R$ {total:.2f}")
print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")