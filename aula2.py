print("12 + 3") # 12 + 3
print(12 + 3) # 15
print("Resultado:", 12 + 3) #resultado: 15
print("12", "3") #12 3

#------ 13 --------------------------------------------------
print("-----------------------------------------------------------------")
nomeOficina = "Robótica pra iniciantes"  #str
sala = "Laboratório 2" # str
quantidadeVagas = 24 # int
duracaoHoras = 2.5 #float
incricoesAbertas = True   #boolean

print(nomeOficina)
print(sala)
print(quantidadeVagas)
print(duracaoHoras)
print(incricoesAbertas)

# ------ 14 --------------------------------------------------
print("-----------------------------------------------------------------")
precoPizza = 48.00 
precoBebida =12.00
quantidadeAmigos = 5

total = precoBebida + precoPizza
divisao = total / quantidadeAmigos

print(f"O total que {quantidadeAmigos} deverão pagar individualmente setrá de: {divisao}")

type(divisao)

#------- 15 ----------------------------------------------------
print("------------------------------------------------------------------")

livrosDispiniveis = 40

print(f"Quantidade inicial de livros disponíveis: {livrosDispiniveis}")
livrosDispiniveis +=12

livrosDispiniveis -= 9
livrosDispiniveis +=4

livrosDispiniveis -=6

print(f"livros atuais disponíveis: {livrosDispiniveis}")

#------- 16 ------------------------------------------------------
print("------------------------------------------------------------------")
# n1 = 7.5
# n2 = 8.0
# n3 = 9.5

nomeAlunos = "Bereceu"
notaAlunoos = [7.5, 8.0, 9.5]

result = (notaAlunoos[0] + notaAlunoos[1] + notaAlunoos[2]) / 3
notaAlunoos[1] = 6.5

print(f"Nota final de {nomeAlunos} é igual a {result}")

#------- 17 ----------------------------------------------------------------
print("--------------------------------------------------------------------")
nome_curso = "Python básico"
mensalidade = 89.90
matricula_aberta = True

print(f"Curso: {nome_curso}")
print(f"Mensalidade: {mensalidade}")
print(f"Vagas abertas: {matricula_aberta}")

type(mensalidade)

# ------- 18 ------------------------------------------------------------------
print("------------------------------------------------------------------------")
saldo = 80
saldo_anterior = saldo

saldo = saldo - 25
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior)  # 80
print("Saldo atual:", saldo) #65

# Isso ocorre pq a variavel 'saldo_anterior' possuia o valor de saldo anteriormente. Quando o saldo foi alterado, a variavel anterior permanecia com o mesmo valor pois não foi lhe atribuido ovamente o valor atualizado de saldo;

#-------- 19 -----------------------------------
quant_alunos = 20
custo_onibus = 600.00
custo_ingresso = 15.00
custo_lanche = 10.00

total_ingressos = custo_ingresso * quant_alunos

total_lanches = custo_lanche * quant_alunos

total_passeio = total_ingressos + total_lanches + custo_onibus

custo_unitario = total_passeio / quant_alunos

print(f"Custo unitário por aluno será de: {custo_unitario}")

# -------- 20 --------------------------------------
print("---------------------------------------------------------------")
informacao = "42"
type(informacao)

informacao = 42
type(informacao)

informacao = 42.0
type(informacao)

informacao = False
type(informacao)

# a diferença é que "42" é uma string, enquanto 42 é um number (int)
# a variável não armazena toos os 4 valores ao mesmo tempo, ela armazena conforme a ordem de atribuições, de cima para baixo

#--------------- 21 ----------------------------------------------------------------
nome = "Atlas"
energia = 100
distancia = 0
amostra = 0
missao_andamento = True

robo = {
    "nome": nome,
    "energia":  energia,
    "distancia_percorrida": distancia,
    "amostras_coletadas": amostra,
    "missao_em_andamento": missao_andamento
}
print(robo)
distancia += 120
energia -=20

amostra +=3
energia -= 15

energia += 10

distancia += 80
energia -=25

amostra += 2
energia -= 10

missao_andamento = False

robo = {
    "nome": nome,
    "energia":  energia,
    "distancia_percorrida": distancia,
    "amostras_coletadas": amostra,
    "missao_em_andamento": missao_andamento,
    "metros_por_minuto": distancia / 4
}

print(robo)