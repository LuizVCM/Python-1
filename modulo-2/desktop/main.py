# Importe a biblioteca 
import tkinter as tk

janela = tk.Tk() # cria janela

janela.title("Primeira janela") # título da interface
janela.geometry("400x300") # define dimensão da interface

texto = tk.Label(
    janela, # interface de ond evai aparecer
    text="bem-vindo", #texto na interface
    font = ("Arial", 30), # fonte com o seu tamanho
    fg= "red"

)

texto.pack(pady=20)

# componentre que permite digitar textos
entrada = tk.Entry(
    janela, # tela que vai
    width=30

)

entrada.pack(pady=10)


def exibir_mensagem():
    print(f"texto: {entrada.get()}")

botao = tk.Button(
    janela, 
text="Clique aqui",
command=exibir_mensagem
)

botao.pack(pady=10)

janela.mainloop() # roda janela