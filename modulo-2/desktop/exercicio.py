import tkinter as tk

tela = tk.Tk()

tela.title("Fotrmulário")
tela.geometry("800x100000")

nomeL = tk.Label(
    tela, 
    text="Digite o seu nome",
    font=("Arial", 30)
    
)
nome = tk.Entry(
    tela,
    width=80,
    fg='red',
    font=("Arial", 30)
)

emailL = tk.Label(
    tela,
    text="Digite o teu email",
    font=("Arial", 30)
)
email = tk.Entry(
    tela,
    width=80,
    fg="blue",
    font=("Arial", 30)
)

cidadeL = tk.Label(
    tela,
    font = ("Arial", 30),
    text="Digite a sua cidade"
)

cidade = tk.Entry(
    tela,
    font=("Arial", 30),
    fg="purple",
    width= 80
)

def mostrar_texto():
    print(f"Olá, {nome.get()}. Seu email é {email.get()} e se encontra na cidade {cidade.get()}!")

botao = tk.Button(
   tela, 
   text="Enviar",
   command=mostrar_texto,
   height=30,
   width=50,
   font=("Serif", 20)

)



nomeL.pack(pady=0)
nome.pack(pady=5)
emailL.pack(pady=25)
email.pack(pady= 5)
cidadeL.pack(pady=25)
cidade.pack(pady = 5)
botao.pack(pady=50)

tela.mainloop()