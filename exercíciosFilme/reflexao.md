O filme O Jogo da Imitação e os programas resolvidos nos mostram que um algoritmo é uma sequência organizada de passos, e que ele precisa prever situações inesperadas, como erros e entradas inadequadas do usuário. Isso mostra que as regras e os testes do sistema são definidos por pessoas, que decidem o que é aceitável ou não. No exercício 2, por exemplo, usamos esta condição:

```
if tempo_disponivel <= 0 or tempo_necessario <= 0:
    print("Tempo inválido!")
else:

```
Com ela, impedimos que o usuário informe valores negativos ou zerados para o tempo. Quanto ao limite da simulação, nosso programa não decifra mensagens criptografadas como acontece no filme. Ele apenas calcula a quantidade de grupos de códigos e o tempo que o analista precisaria para realizar a descriptografia.