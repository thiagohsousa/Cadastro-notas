from funcoes import procedimentomenu
from funcoes import calcularmedia

procedimentomenu()

nome = []
notaum = []
notadois = []


# Coleta de dados
for i in range(4):
    nome_temp = input("Qual é o nome do aluno?\n")
    notaum_temp = float(input("Qual é a primeira nota?\n"))
    notadois_temp = float(input("Qual é a segunda nota?\n"))

    nome.append(nome_temp)
    notaum.append(notaum_temp)
    notadois.append(notadois_temp)

# Calcula a média com base nas listas preenchidas
nota = calcularmedia(notaum, notadois)

# Exibe resultado
for i in range(4):
    if nota[i] < 7:
        print(f"{nome[i]} você está Reprovado!!! com a média de {nota[i]:.2f}")
    else: 
        print(f"{nome[i]} você está Aprovado!!! com a média de {nota[i]:.2f}")
