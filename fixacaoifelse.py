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
