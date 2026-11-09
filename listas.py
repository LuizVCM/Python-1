#ex1
lista1 = ["abajur","Ácido desoxibonucleico", "fatias", "lâminas", "espátulas"]
print(lista1)
print(len(lista1))
print(lista1[0])
print(lista1[-1])

#ex2
lista2 = []
print("--------------------------")
item1 = input("Digite o primeiro elemento: ")
lista2.append(item1)

item2 = input("Digite o segundo elemento: ")
lista2.append(item2)

item3 = input("Digite o terceiro elemento: ")
lista2.append(item3)

item4 = input("Digite o quarto elemento: ")
lista2.append(item4)

print(lista2)

#ex3

print("----------------------------------")

numeros = []
pergunta = 0
soma = 0

for resposta in range(0, 6, +1):
    pergunta = int(input(f"Digite o {resposta+1}° número: "))

    numeros.append(pergunta)

for item in numeros:
    soma += item

media = soma/len(numeros)

print(f"\n\nLista completa: {numeros}\n")
print(f"Soma dos elementos: {soma}")
print(f"Média dos números: {media}")
print(f"maior número: {max(numeros)}")
print(f"menor número: {min(numeros)}")

#ex4
print("-------------------------------------")

elementos = ["corda", "água", "mapa", "água"]

for item in elementos:
    print(f"Elemento analisado: {item}")
    aparicao = 0
    for copia in elementos:
        if copia == item:
            aparicao += 1
    print(f"\n {item} aparece {aparicao} vezes!\n\n")
 
#ex5
print("-------------------------------------")

numeros1 = []
pares = []

for num in range(0, 8, +1):
    num = int(input(f"Digite o {num+1}° número: "))
    numeros1.append(num)

for item in numeros1:
    if item % 2 == 0:
        pares.append(item)

print(f"Lista original: {numeros1}")
print(f"lista com pares: {pares}")

#ex6
print("---------------------------------------")

nome = input("Digite um nome para remover da lista: ")

nomes = ["Ana", "Bruno", "Ana", "Carla"]
print(f"quantidade atual: {len(nomes)}")
print(nomes)

if nome in nomes:
    nomes.remove(nome)
    print("Removido com sucesso!!\n")
else:
    print(f"Nome '{nome}' inexistente na lista!")

print(f"quantidade recente: {len(nomes)}")
print(nomes)

#ex7
print("----------------------------------------------")

quantidade_alunos = int(input("Digite a quantidade de alunos: "))
nota = 0
notas = []
soma = 0
maior_sete = 0

if quantidade_alunos <= 0:
    print("Quantidade inválida!")
else:
    for aluno in range(0, quantidade_alunos, +1):
        nota = float(input(f"Digite a nota do {aluno+1}° aluno: "))
        while nota < 0 or nota > 10:
            nota = float(input(f"Digite novamente a nota do {aluno+1}° aluno: "))
        notas.append(nota)
        print(f"nota do {aluno}° aluno armazenada com sucesso!\n")
    for element in notas:
        soma += element
        if element >=7:
            maior_sete += 1

    print(f"Notas: {notas}")
    print(f"média da notas: {soma/quantidade_alunos}")
    print(f"maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")
    print(f"quantidade de notas maiores que 7: {maior_sete}")

#ex8
print("----------------------------------------------------------")

fila = []

while True:
    print("\n1 - Adicionar pessoa ao final da fila")
    print("2 - Atender a primeira pessoa")
    print("3 - Mostrar a fila e sua quantidade de pessoas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da pessoa: ")
        fila.append(nome)
        print(f"{nome} foi adicionado(a) ao final da fila.")

    elif opcao == "2":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Atendendo: {atendido}")
        else:
            print("A fila está vazia. Ninguém para atender.")

    elif opcao == "3":
        print(f"Fila: {fila}")
        print(f"Quantidade de pessoas: {len(fila)}")

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida! Tente novamente.")

# 9
pontuacoes = []

while True:
    print("\n--- MENU ---")
    print("1 - Registrar pontuação")
    print("2 - Mostrar relatório")
    print("3 - Desfazer o último registro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        while True:
                pontv = int(input("Digite a pontuação (0 a 100): "))
                if 0 <= pontv <= 100:
                    pontuacoes.append(pontv)
                    print("Pontuação registrada com sucesso!")
                    break
                else:
                    print("Erro: O valor deve estar entre 0 e 100.")

    elif opcao == '2':
        if len(pontuacoes) == 0:
            print("Não há missões registradas.")
        else:
            quantidade = len(pontuacoes)
            total = sum(pontuacoes)
            media = total / quantidade
            maior = max(pontuacoes)

            acima_ou_igual_70 = sum(1 for p in pontuacoes if p >= 70)

            print("\n--- RELATÓRIO DE MISSÕES ---")
            print(f"Pontuações na ordem de registro: {pontuacoes}")
            print(f"Quantidade de missões: {quantidade}")
            print(f"Total de pontos: {total}")
            print(f"Média das pontuações: {media:.2f}")
            print(f"Maior pontuação: {maior}")
            print(f"Missões com pelo menos 70 pontos: {acima_ou_igual_70}")

    elif opcao == '3':
        if len(pontuacoes) == 0:
            print("Não há registro para desfazer.")
        else:
            removido = pontuacoes.pop()
            print(f"Registro desfeito com sucesso! Pontuação removida: {removido}")

    elif opcao == '0':
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida do menu.")