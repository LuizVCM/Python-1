# 1
horas = int(input("Quantas horas? "))
preco = 0

if horas> 0 and horas <=2:
    preco = 10
    print(f"{preco} reais")
elif horas > 2 and horas <=5:
    preco = 20
    print(f"{preco} reais")
elif horas > 5:
    preco = 30
    print(f"{preco} reais")
else:
    print("Sem valor para pagar!") 

# 2

nome = input("Digite o nome de seu personagem: ")
nivel = int(input(f"Digite o nível do personagem {nome}: "))

if nivel >=1 and nivel <=5:
    print(f"personagem {nome} com classificação aprendiz")
elif nivel > 5 and nivel <=15:
    print(f"personagem {nome} com classificação guerreiro")
elif nivel > 15 and nivel <=30:
    print(f"personagem {nome} com classificação veterano")
elif nivel > 31:
    print(f"personagem {nome} com classificação lendária")
else:
    print(f"personagem {nome} com nível inválido!")

# 3
usuario = input("Digite o seu usuário: ").lower
senha = input("Digite a sua senha: ").lower

if usuario == "admin" and senha == "python123":
    print("Acesso autorizado!")
elif usuario == "admin" and senha != "python123":
    print("Acesso negado. Senha incorreta! ")
else:
    print("Acesso negado.")

# 4
salario = float(input("Digite a média de seu salário: "))
emprestimo = float(input("Digite o empréstimo solicitado: "))
parcelas = int(input("Digite a quantidade de parcelas que desejar: "))

if salario < 2000.00:
    print("Salário muito baixo. Informe um salário maior!")
elif emprestimo > 10*salario:
    print("Empréstimo acima do possível!")
elif emprestimo/parcelas > 30*(salario/100):
    print("Parcelas não autorizadas.")
elif parcelas < 1 or parcelas >48:
    print("Quantidade de parcelas inválidas!")
else:
    print("requisição aceita")

# 5
nomeP = input("Digite o nome de seu personagem: ")
vidaAtual = int(input("Digite a vida atual de seu personagem: "))
pontosAtaque = int(input("Diga os pontos de ataque de ataque: "))

vidaInimigo = int(input("Digite a vida de seu inimigo: "))
pontosDefesa = int(input("Digite a defesa de seu inimigo: "))

dano = pontosAtaque - pontosDefesa

if vidaAtual <= 0:
    print("Erro crítico no ataque!")
elif dano <= 0:
    print("Dano inimigo: Miss")
elif dano >= vidaInimigo:
    print("Inimigo derrotado")
    vidaInimigo = 0
else:
    print(f"Dano concebido. {vidaInimigo}")

# 6
year = int(input("Digite a sua idade: "))
matriculass = input("Possui matrícula? (sim/não) ").lower
autorizacaos = input("Possui autorização de professor? (sim/não) ").lower
laboratorio_disponivel = input("Possui laboratório disponível? (sim/não) ").lower

if laboratorio_disponivel == "sim" and year >=16 and (matriculass == "sim" or autorizacaos == "sim"):
    print("Acesso autorizado!!")
else:
    print("Acesso negado!")

# 7
valor_regiao = input("Digite a região do Brasil (sul, norte, nordeste, sudeste ou centro oeste): ").lower()
valor_compra = int(input("Digite o valor total da compra: "))

valor_final = 0

if valor_compra <= 0:
    print("Valor inválido!\n")
elif valor_regiao != "sul" and valor_regiao != "norte" and valor_regiao != "nordeste" and valor_regiao != "sudeste" and valor_regiao != "centro oeste":
    print("Região inválida!\n")
else:
    if valor_compra >= 300:
        valor_final = valor_compra
    else:
        if valor_regiao == "sul":
            valor_final = valor_compra + 15
        elif valor_regiao in ["norte", "nordeste"]:
            valor_final = valor_compra + 35
        elif valor_regiao == "centro oeste":
            valor_final = valor_compra + 25
        else:  # sudeste
            valor_final = valor_compra + 20

    print(f"Valor final: {valor_final}")

# 8

ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

if ladoA*ladoB*ladoC < 0:
   print("Dados incorretos! ")
elif ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoC + ladoA > ladoB:
        if ladoA == ladoB and ladoB == ladoC and ladoA == ladoC:
            print("Os dados formam um triângulo equilátero!")
        elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
            print("Os dados formam um triângulo isósceles! ")
        else:
            print("Os dados formam um triângulo escaleno!")
else:
    print("valores não formam um triângulo!")    