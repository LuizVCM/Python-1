#1 

class livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

livro1 = livro("Livro 1", "Eu, Carlinhos Maia", 45)
livro2 = livro("Livro 2", "Tu", 20)

print(livro1.paginas)
print(livro2.paginas)

livro2.paginas = 99

print(livro1.paginas)
print(livro2.paginas)

# a classe é o livro e os objetos são o livro1 e livro2
# os atributos são as páginas, o autor e o nome

# 2
print("-------------------------------------------")

class retangulo:
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura

def calcular_area(self):
    return self.largura * self.altura

objeto1 = retangulo(10, 20)
objeto2 = retangulo(10, 11)

print(calcular_area(objeto1))
print(calcular_area(objeto2))

# return literalmente atribui um valor à função, enquanto mostrá-la dentro da função não atribuiria nenhum valor à função, apenas exprimiria um valor

# 3
print("----------------------------------------------------------")

class contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1
        return self.valor

    def zerar(self):
        self.valor *= 0
        return self.valor

contador1 = contador()
contador2 = contador()

print(contador1.valor, contador2.valor)


contador1.incrementar()
contador1.incrementar()
contador1.incrementar()

contador2.incrementar()
print(contador1.valor, contador2.valor)

contador1.zerar()

print(contador1.valor, contador2.valor)

# 4
print("------------------------------------------------------")

class Produto:
    def __init__(self, valor, estoque):
        self.valor = valor
        self.estoque = estoque

    def repor(self):
        quantidade = int(input("Quantas unidades deseja repor? "))
        self.estoque += quantidade
        self.valor *= self.estoque
        return self.estoque

    def vender(self):
        quantidade = int(input("Quantas unidades deseja vender?"))
        self.estoque -= quantidade
        
        


        
