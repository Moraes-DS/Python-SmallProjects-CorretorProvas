#Programa de correção de provas objetivas

# Inicializamos os dados
respostas = []  # Lista para receber as respostas
nota = 0  # Acumula a nota total

# Recebendo o gabarito da prova
gabarito = []
print("Insira o gabarito da prova:")
for i in range(10):
    gabarito.append(input(f"Insira a resposta do gabarito para a questão {i + 1}: ").upper())

#Enquanto houver alunos a serem corrigidos
continuar = "S"
while continuar == "S":
    #Recebendo o nome do aluno
    nome_aluno = input("Insira o nome do aluno: ")

    #Recebendo as respostas do aluno
    respostas.clear()  # Limpando respostas anteriores
    print(f"Insira as respostas do aluno {nome_aluno}:")
    for i in range(10):
        respostas.append(input(f"Insira a resposta da questão {i + 1}: ").upper())

    #Verificando as respostas e calculando a nota
    nota = 0
    for i in range(10):
        if respostas[i] == gabarito[i]:
            nota += 1

    #Exibindo a nota final
    print(f"Aluno: {nome_aluno}")
    print(f"Nota final: {nota}")

    #Perguntando se deseja corrigir a prova de outro aluno
    continuar = input("Deseja corrigir a prova de outro aluno? (S/N): ").upper()

print("Programa encerrado.")