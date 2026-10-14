from datetime import datetime
#ex 1

nome = input("Digite o seu nome: ")
cidade = input("Digite a sua cidade: ")
idade = int(input("Digite a sua idade: "))

year_birth = (datetime.now().year) - idade

ano_que_vem = datetime.now().year - year_birth + 1

print(f"Você, {nome}, cidadão(ã) de {cidade}, terá {ano_que_vem} no ano de {datetime.now().year + 1}\n\n\n")

# ex2

preco = float(input("Digite o preço do lanche: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

if total < 0:
    print("Valor inválido!!! dicione apenas valores positivos!\n\n")
elif total >= 50.00:
    print(f"Valor antes do desconto: {total}\n\n\n\n")
    total -= total* 0.10
    print(f"Valor total após o desconto: {total}\n\n\n")
else: 
    print(f"Valor total: {total}\n\n")


# ex3

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segungo número: "))

if n1 > n2:
    print(f"o primeiro número, {n1}, é maior!!!!!!!!!!!!!!!")
elif n2> n1:
    print(f"O segundo número, {n2}, é maior!!!!!!!!!!!!!!!!")
else:
    print(f"Os dos números, {n1} e {n2}, são iguais!!!!!!!!")


# ex4

temperatura = float(input("Digite a temperatura do ambiente em graus Célsios: "))

if temperatura < 18:
    print(f"O ambiente está frio!!!\n\n\n\n")
elif temperatura >=18 and   temperatura < 26:
    print(f"Ambiente com temperatura agradável!\n\n\n")
else:
    print("Ambiente com temperatura pelando!!!!\n\n\n\n")


# ex5

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

if (nota1 < 0 and nota1 > 10) or (nota2 < 0 and nota2 > 10):
    print("Cálculo de média inválido!!! Adicione notas entre 0 e 10!")
elif (nota1 + nota2)/2 >= 7:
    print("aprovado \n\n\n\n\n")
elif (((nota1 + nota2)/2) >= 5) and (((nota1 + nota2)/2) < 7):
    print("recuperação \n\n\n\n\n")
elif ((nota1 + nota2)/2) < 5:
    print("Reprovado!!!!!!!!!!!!!!!!!\n\n\n\n")

#ex 6

idade2 = int(input("Digite a sua idade: "))
inscricao = input("Fez inscrição (sim, não) ")

if inscricao.lower() == "não":
    inscricao = False
else:
    inscricao = True

if idade < 0:
    print("Idade inválida!!\n\n\n")


if idade >= 14 and inscricao:
    print("Entrada liberada!!!!!!!")
else:
    print("Entrada barrada")

#ex7

idade3 = int(input("Digite a sua idade: "))

if idade3 < 0:
    print("Idade inválida!!!!!!!!!!\n\n\n\n\n")
elif idade3 < 12 or idade3 >= 60:
    print("Acesso liberado. Ingresso gratuito!!!\n\n\n\n\n\n\n")
else:
    print("Acesso liberado. Ingressos por R$ 20,00 \n\n\n\n")

#ex8

quantidade_livros = int(input("Digite a quantidade de livros "))
quantidade_exemplar = 8

if quantidade <=0:
    print("pedido invalido!!!!! \n\n\n\n\n")
elif quantidade_livros > quantidade_exemplar:
    print("Não há exemplares suficientes!!!!!!!!\n\n\n")
else:
    print(f"Pedido confirmado. Estoque restante: {quantidade_exemplar - quantidade_livros}\n\n\n")

#ex9

decimal1 = float(input("Digite o primeiro número: "))
decimal2 = float(input("Digite o segundo número: "))

operador = input("Digite '1' para somar, '2' para subtrair, '3' para multiplicar ou '4' para dividir: ")

if operador == '1':
    print(f"Soma: {decimal1 + decimal2}\n\n\n")
elif operador == '2': 
    print(f"Subtração: {decimal1 - decimal2}\n\n\n")
elif operador == '3':
    print(f"Multiplicação: {decimal1 * decimal2}\n\n\n")
elif operador == '4':
    if decimal2 == 0:
        print("Divisão por 0 inválida!!!!!\n\n\n")
    else:
        print(f"Divisão: {decimal1 / decimal2}\n\n\n")
else:
    print("Informação inválida!!!!\n\n\n\n")

#ex10
idade10 = int(input("Digite a sua idade: "))
autorizacao = input("Possui autorização? (sim/não) ")

if autorizacao.lower == "não":
    autorizacao = False
else:
    autorizacao = True

if idade10 >= 16 and autorizacao:
    print("Participação permitida!\n\n\n")
else:
    print("Participação nçao permitida!!\n\n\n")


