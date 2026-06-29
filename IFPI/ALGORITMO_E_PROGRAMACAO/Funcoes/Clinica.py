# 7 - Clínica

def valor_base_consulta(tipo):
    if tipo == "normal":
        return 100
    elif tipo == "retorno":
        return 60
    elif tipo == "urgencia":
        return 180
    else:
        return 0

def valor_final_consulta(tipo, convenio):
    valor = valor_base_consulta(tipo)
    if convenio:
        valor *= 0.70
    return valor

def gerar_resumo_atendimento(nome, tipo, convenio):
    valor_final = valor_final_consulta(tipo, convenio)
    resumo = f"""
--- RESUMO DO ATENDIMENTO ---
Paciente: {nome}
Tipo de consulta: {tipo}
Valor final: R$ {valor_final:.2f}
"""
    return resumo

nome = input("Digite o nome do paciente: ")
tipo = input("Tipo de consulta (normal/retorno/urgencia): ").strip().lower()
convenio_input = input("Possui convênio? (s/n): ").strip().lower()
convenio = convenio_input == "s"

print(gerar_resumo_atendimento(nome, tipo, convenio))