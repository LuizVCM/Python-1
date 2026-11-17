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
        return "estoque:", self.estoque

    def vender(self):
        quantidade = int(input("Quantas unidades deseja vender?"))
        
        if self.estoque <=0 or quantidade >self.estoque:
            return "Não foi possível efetuar"
        else:
            self.estoque -= quantidade
            return self.estoque
    def total(self):
        total = self.quantidade * self.estoque
        return "total:", total 

produto1 = Produto(5.00, 4)

print(produto1.vender())
print(produto1.repor())

print(f"Estoque completo: {produto1.estoque} com {produto1.estoque*produto1.valor} reais")

# 5
print("------------------------------------------------------------")
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return True
        return False

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return True
        return False
    
livro1 = Livro("Teste 1")
print(livro1.emprestar())  
print(livro1.emprestar())  
print(livro1.devolver())   
print(livro1.devolver())

# 6
print("-----------------------------------------------")

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = [] 

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)

t1 = Turma("Matemática")
t1.matricular("Ana")
print(t1.nome, t1.alunos)

# 7
print("----------------------------------------------------")

class Produto:
    def __init__(self, nome, valor, estoque):
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

produtos = [
    Produto("Caderno", 10.0, 2),
    Produto("Caneta", 3.0, 0),
    Produto("Borracha", 2.0, 5)
]

total = 0
sem_estoque = 0

for p in produtos:
    valor_total_prod = p.valor * p.estoque
    total += valor_total_prod
    if p.estoque == 0:
        sem_estoque += 1
    print(f"{p.nome} - Estoque: {p.estoque} - Valor em estoque: {valor_total_prod}")

print(f"Total geral: {total}")
print(f"Produtos sem estoque: {sem_estoque}")

# 8
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

c = Conta("Alice")
print(c.depositar(50))  
print(c.sacar(20))      
print(c.sacar(40))      
print(c.saldo)          
    
        
        


        
