identificacao = input("Digite o identificação da mensagem: ")
tempo_disponivel = float(input("Digite o tempo disponível: "))
tempo_necessario = float(input("Dgite o tempo necessário: "))
risco = input("A mensagem indica risco imediato? (sim/nao): ")
pista = input("A mensagem contém uma pista recorrente? (sim/nao): ")

tempo_restante = tempo_disponivel - tempo_necessario

if tempo_restante <=0:
     tempo_restante = 'Sem tempo disponível!'

if tempo_disponivel <= 0 or tempo_necessario <= 0:
     print("Tempo inválido!")
else:
     if (risco != 'sim' and risco != 'não') or (pista != 'sim' and pista != 'não'):
          print("Resposta inválida!") 
     else:
          if tempo_necessario > tempo_disponivel:
               situacao = "Solicitar apoio: tempo insuficiente"
               print("------ Relatório ------")
               print(f"\n identificação: {identificacao}\nresultado: {situacao}\n\n Tempo restante em min: {tempo_restante}")
          elif tempo_necessario <= tempo_disponivel and risco == 'sim':
               situacao = "Prioridade máxima"
               print("------ Relatório ------")
               print(f"\n identificação: {identificacao}\nresultado: {situacao}\n\n Tempo restante em min: {tempo_restante}")
          elif tempo_necessario <= tempo_disponivel and risco == 'não' and pista == 'sim':
               situacao = "Prioridade alta"
               print("------ Relatório ------")
               print(f"\n identificação: {identificacao}\nresultado: {situacao}\n\n Tempo restante em min: {tempo_restante}")
          elif tempo_necessario <= tempo_disponivel and risco == 'não' and pista == 'não':
               situacao = "Prioridade normal"  
               print("------ Relatório ------")
               print(f"\n identificação: {identificacao}\nresultado: {situacao}\n\n Tempo restante em min: {tempo_restante} minutos")

               