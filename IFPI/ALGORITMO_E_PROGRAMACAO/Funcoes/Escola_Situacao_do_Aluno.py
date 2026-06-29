# 4 - Escola: Situação do Aluno

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def calcular_frequencia(presencas, aulas):
    if aulas <= 0:
        return 0
    return (presencas / aulas) * 100

def definir_situacao_final(notas, presencas, aulas):
    media = calcular_media(notas)
    frequencia = calcular_frequencia(presencas, aulas)

    if frequencia < 75:
        return "Reprovado por falta"
    elif media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

entrada_notas = input("Digite as notas separadas por vírgula: ")
notas = [float(nota.strip()) for nota in entrada_notas.split(",")]

presencas = int(input("Digite o número de presenças: ").strip())
aulas = int(input("Digite o número total de aulas: ").strip())

media = calcular_media(notas)
frequencia = calcular_frequencia(presencas, aulas)
situacao = definir_situacao_final(notas, presencas, aulas)
print("--- RESULTADO ---")
print(f"Média: {media:.2f}")
print(f"Frequência: {frequencia:.2f}%")
print(f"Situação final: {situacao}")