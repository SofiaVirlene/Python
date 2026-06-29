# Agricultura: Irrigação

def media_umidade(sensores):
    return sum(sensores) / len(sensores)

def decidir_irrigacao(sensores, limite):
    return media_umidade(sensores) < limite

def mensagem_irrigacao(sensores, limite):
    return "Irrigar agora" if decidir_irrigacao(sensores, limite) else "Não irrigar"

quantidade = int(input("Quantos sensores deseja informar? "))

sensores = []

for i in range(quantidade):
    valor = float(input(f"Digite a umidade do sensor {i+1}: "))
    sensores.append(valor)

limite = float(input("Digite o limite mínimo de umidade: "))

media = media_umidade(sensores)
mensagem = mensagem_irrigacao(sensores, limite)

print("--- SISTEMA DE IRRIGAÇÃO ---")
print("Valores dos sensores:", sensores)
print(f"Média de umidade: {media:.2f}")
print(mensagem)