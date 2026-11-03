# # ex1
# numero = int(input("Digite um número positivo: "))

# if numero <=0:
#     print("Número inválido!\n\n")
# else:
#     for n in range(0, numero, +1):
#         print(f"número {n}")

# # ex2
# print("----------------------------------------------------")
# numero2 = int(input("\nDigite um número positivo: "))

# if numero2 <=0:
#     print("Número inválido!\n")
# else:
#     for n1 in range(numero2, 0, -1):
#         print(f"Número {n1}")
#     print("Lançamento realizado!\n")

# #ex3
# print("--------------------------------")

# numero3 = int(input("Digite um número inteiro positivo: "))

# if numero3 <= 0 or numero3 == 1:
#     print("Sem análise!")
# else:
#     for n4 in range(0, numero3, +2):
#         print(f"número par: {n4}")

# #ex4
# print("---------------------------------")

# tabuada = int(input("Informe um número inteiro para verificar a sua tabuada: "))

# for fator in range(0, 11, +1):
#     print(f"{tabuada} X {fator} = {tabuada*fator}")

# # ex5
# print("-----------------------------------")

# soma = 0
# contador = 0

# for num in range(0, 6, +1):
#     nums = int(input("Digite um número positivo inteiro: "))

#     soma += nums
#     if nums > 0:
#         contador +=1

# print(f"Soma total: {soma}")
# print(f"Maiores que zero: {contador}")

# #ex6
# print("----------------------------------------")

# alunos = int(input("Digite a quantidade total de alunos: "))
# soma = 0
# alunos_sete = 0
# if alunos <=0:
#     print("Quantidade inválida.")
# else:

#     for aluno in range(1, alunos+1, +1):
#         nota = float(input(f"Digite a nota do aluno {aluno}: "))

#         while nota < 0 or nota > 10:
#             nota = float(input(f"Digite novamente a nota do aluno {aluno}: "))

#         soma += nota

#         if nota >= 7:
#             alunos_sete += 1
#     print("nota armazenada!")
#     print("-------")

# print(f"Média: {soma/alunos}")
# print(f"Alunos com nota maior que sete: {alunos_sete}")

# #ex7

# print("---------------------------------------")

# texto = input(" Digite uma frase ou palavra: ")
# letra_especial = input("Digite um caractere para contabilizar: ")
# aparecer = 0

# for letra in texto:
#     if letra == letra_especial:
#         aparecer += 1

# print(f"Quantas vezes a letra '{letra_especial}' apareceu foi {aparecer} vezes!")

# #ex8

codigo = "ROBO123"
tentativas_total = 3

for tentativa in range(1, tentativas_total + 1, +1):
    print(f"Tentativa {tentativa} de {tentativas_total}")
    palpite = input("Digite o código: ")

    if palpite== codigo:
        print("Código correto! Acesso liberado.")
        break
    else:
        print("Código incorreto.")
else:
    print("As tentativas acabaram. Acesso bloqueado.")
    print(f"senha correta: {codigo}")