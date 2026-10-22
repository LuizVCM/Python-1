# # 1
# numero = int(input("Informe um numero de itens: "))

# i = 1

# while i <= numero:
#     print(f"Aqui está o seu item {i}\n")
#     i+= 1

# # 2
# print("---------------------------------------------")

# numero2 = int(input("Informe um número de segundos: "))

# i2 = 0

# while numero2 >= i2:
#     print(numero2)

#     numero2 -= 1

# # 3
# print("-----------------------------------------------")
# multiplicador = int(input("Informw um número para cosultar a tabuada: "))

# i3 = 0

# while i3 <= 10:
#     print(f" {i3} x {multiplicador} = {i3*multiplicador}")
#     i3 += 1

# # 4
# print("------------------------------------------------")

# i4 = 1
# soma = 0

# while i4 <= 5:
#     pergunta = int(input("Informe um número: "))
#     soma += pergunta

#     i4 += 1

# print(f"Soma total: {soma}")

# # 5

# print("-------------------------------------------------")
# alunos = int(input("Digite quantos alunos: "))
# notas = 0
# indice = 1

# while indice <= alunos:
#     nota = float(input(f"Digite a nota do aluno {indice}: "))
#     notas += nota

#     indice += 1

# media = notas/alunos
# print(f"total: {notas}\n")
# print(f"Média da turma: {media} pontos!")

# # 6

# print("----------------------------------------------------------------------")

# situacao = "nota inválida"

# while situacao == "nota inválida":
#      notasss = float(input("Digite uma nota de 0 a 10: "))

#      if notasss >= 0 and notasss <= 10:
#          situacao = "nota válida!"
#      else:
#          print("\n nota inválida! \n")
#          situacao = "nota inválida"

# print(f"nota {notasss} registrada com sucesso!")

# # 7
while True:

    print("Escolha uma ds opções abaixo: \n")
    print("1 - somar dois números")
    print("2 - verificar maioridade")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print(f"A soma é: {n1+n2}")

    elif opcao == 2:
        idade = int(input("Digite sua idade: "))
        if idade >=18:
            print("menor de idade")
        elif idade < 0:
            print("idade inválida")
        else:
            print("menor de idade")
    elif opcao == 0:
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
