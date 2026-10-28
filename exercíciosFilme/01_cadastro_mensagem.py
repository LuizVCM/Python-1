nome = input("Digite o seu nome: ")
identificacao = input("Digite a sua identificação: ")
quantidade = int(input("Digite a quantidade de grupos: "))
tempo = float(input("Digite o tempo estimado: "))

if quantidade < 0 and tempo < 0 :
     print("Dados inválidos!")
elif quantidade >= 0 and tempo >= 0:
     tempoTotal = quantidade*tempo

     print("------ Ficha ------")
     print(f"analista: {nome}\nidentificação: {identificacao}\nquantidade de grupos: {quantidade}\ntempo total: {tempoTotal}\n\n")
else:
     print("informações incorretas!")
          

     