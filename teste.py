from re import T
from tkinter import *
from tokenize import Number
from classes.Persons.Cliente import Cliente
from classes.Finances.Compra import Compra
from classes.Finances.Conta import Conta
from classes.Utilities.Contrato import Contrato
from classes.Utilities.Endereco import Endereco
from classes.Produtcs.Estoque import Estoque
from classes.Persons.Funcionarios import Atendente, Entregador
from classes.Produtcs.Item import Item
from classes.Produtcs.Produto import Produto

'''classe responsável da tela de estoque'''


class Main:
    '''init responsável por inicializar as variaveis, o tamanho da tela, onde será posicionado e os titulos dos produtos, ex: nome, id, etc'''

    def __init__(self, window):
        self.janela = janela
        self.janela.title("Estoque")

        largura = 1280
        altura = 720

        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.janela.iconbitmap("assets/images/shopping-cart-icon.ico")
        self.janela.resizable(0, 0)

        self.container = Frame(self.janela)
        self.container.grid(row=1, column=0)
        self.labelNome = Label(
            self.container, text="Nome", bg='lightgreen', padx=50)
        self.labelNome.grid(row=2, column=0, padx=15, pady=5)

        self.labelId = Label(self.container, text="ID", bg='white', padx=50)
        self.labelId.grid(row=2, column=1, padx=15, pady=5)

        self.labelPreco = Label(
            self.container, text="Preço", bg='lightgreen', padx=50)
        self.labelPreco.grid(row=2, column=2, padx=15, pady=5)

        self.labelDataVal = Label(
            self.container, text="Data de validade", bg='white', padx=50)
        self.labelDataVal.grid(row=2, column=3, padx=15, pady=5)

        self.labelDataFab = Label(
            self.container, text="Data de fabricação", bg='lightgreen', padx=50)
        self.labelDataFab.grid(row=2, column=4, padx=15, pady=5)

        self.labelQtdNoEstoque = Label(self.container, text="Quantidade no estoque",
                                       bg='white')
        self.labelQtdNoEstoque.grid(row=2, column=5, padx=15, pady=5)

        self.updateStorage()
        self.containerButton = Frame(self.janela)
        self.containerButton.grid(row=2, column=0)
        buttonRemove = Button(
            self.containerButton, text="Remover Produto", command=self.removerProduto, bg="orange", fg="white", pady="10px", padx="10px")
        buttonRemove.grid(row=20, column=7, pady=10, padx=10)
        buttonRestock = Button(
            self.containerButton, text="Reabastecer Produto", bg="orange", command=self.reabastecerEstoque, fg="white", pady="10px", padx="10px")
        buttonRestock.grid(row=20, column=6, pady=10, padx=10)

        button2 = Button(self.containerButton, text="Adicionar produto",
                         command=self.adicionarNovoProduto, bg="orange", fg="white", pady="10px", padx="10px")
        button2.grid(column=5, row=20, padx=(800, 10), pady=10)
        '''Metodo é usado quando o usuario digita um id inválido ao reabastecer ou remover um produto'''

    def erro(self, validante):
        if(validante == 0):
            self.view = Tk()
            self.view.title("Erro")

            largura = 350
            altura = 70

            largura_screen = self.view.winfo_screenwidth()
            altura_screen = self.view.winfo_screenheight()

            posx = largura_screen/2 - largura/2
            posy = altura_screen/2 - altura/2

            self.view.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
            self.view.iconbitmap("assets/images/shopping-cart-icon.ico")
            self.view.resizable(0, 0)
            self.container = Frame(self.view)
            self.container.grid(row=1, column=0)

            self.labelNome = Label(
                self.container, text="Produto não encontrado", font=("sans-serif", 24))
            self.labelNome.grid(row=2, column=1)
            self.view.mainloop()
        '''metodo usado sempre que precisamos aumentar, reabastecer ou remover elemento para que os dados sejam atualizados'''

    def updateStorage(self):

        for x in range(len(estoque.get_produtos())):

            self.labelNome = Label(self.container, text=estoque.get_produtos()[
                x].get_nome(), bg='lightgreen', width=10, padx=10)
            self.labelNome.grid(row=x+3, column=0)

            self.labelId = Label(self.container, text=estoque.get_produtos()[
                x].get_id(), bg='white', width=10)
            self.labelId.grid(row=x+3, column=1)

            self.labelPreco = Label(self.container, text=estoque.get_produtos()[
                x].get_preco(), bg='lightgreen', width=10, padx=10)
            self.labelPreco.grid(row=x+3, column=2)

            self.labelDataVal = Label(self.container, text=estoque.get_produtos()[
                x].get_data_validade(), bg='white', width=10)
            self.labelDataVal.grid(row=x+3, column=3)

            self.labelDataFab = Label(self.container, text=estoque.get_produtos()[
                x].get_data_fabricacao(), bg='lightgreen', width=10)
            self.labelDataFab.grid(row=x+3, column=4)

            self.labelQtsNoEstoque = Label(self.container, text=estoque.get_produtos()[
                x].get_quantidade_estoque(), bg='white', width=10)
            self.labelQtsNoEstoque.grid(row=x+3, column=5)

    '''tela responsável pelas informações do produto que sera removido, no caso um input para o id e um botão de remoção '''

    def removerProduto(self):
        self.view = Tk()
        self.view.title("Adicionar Produto")

        largura = 1280
        altura = 720

        largura_screen = self.view.winfo_screenwidth()
        altura_screen = self.view.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.view.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.view.iconbitmap("assets/images/shopping-cart-icon.ico")

        labelid = Label(self.view, text="ID do produto: ",
                        font=("sans-serif", 16))
        labelid.grid(row=0, column=0)

        self.inputProduto = Text(self.view, width=60, pady="8px",
                                 padx="8px", height=1, font=("sans-serif", 16))
        self.inputProduto.grid(row=0, column=1)

        self.button1 = Button(self.view, text="Remover", command=self.removeProduct,
                              bg="orange", fg="white", pady="10px")
        self.button1.grid(column=10, row=7)

        self.view.mainloop()
        '''Método que serve para criar um novo produto, criamos uma instancia de produtos e adicionamos no estoque'''

    def createNewProduct(self):
        # print(self.inputId.get("1.0", END), self.inputNome.get("1.0", END), self.inputPreco.get("1.0", END), self.inputDataVal.get("1.0", END), self.inputDataFab.get("1.0", END))
        newProduct = Produto(int(self.inputId.get("1.0", END)), str(self.inputNome.get("1.0", END)), float(self.inputPreco.get(
            "1.0", END)), self.inputDataVal.get("1.0", END), self.inputDataFab.get("1.0", END), int(self.inputQtdNoEstoque.get("1.0", END)))
        estoque.adicionarNovoProduto(newProduct)
        self.updateStorage()
    '''metodo para remover os produtos de estoque e caso o id não exista aprece uma tela de erro, e se existir o produto será removido'''

    def removeProduct(self):
        a = estoque.get_instancia(int(self.inputProduto.get("1.0", END)))
        if(a == 0):
            self.erro(a)
        else:
            estoque.removerProduto(a)
            self.container.destroy()
            Main(janela)
            self.updateStorage()
    '''usa um metodo de pegar uma instancia e passa para reabastecer um produto e aumenta a quantidade do produto no estoque ou diminui'''

    def restockProduct(self):
        a = estoque.get_instancia(int(self.inputProduto.get("1.0", END)))
        estoque.reabastecerEstoque(
            a, int(self.inputQuantidade.get("1.0", END)))
        self.erro(a)
        self.updateStorage()
    '''tela com os inputs para identificar qual produto sera reabastecido e a quantidade'''

    def reabastecerEstoque(self):
        self.view = Tk()
        self.view.title("Reabastecer Produto")

        largura = 1280
        altura = 720

        largura_screen = self.view.winfo_screenwidth()
        altura_screen = self.view.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.view.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.view.iconbitmap("assets/images/shopping-cart-icon.ico")
        labelProduto = Label(self.view, text="Id do produto: ",
                             font=("sans-serif", 16))
        labelProduto.grid(row=0, column=0)

        self.inputProduto = Text(self.view, width=60, pady="8px",
                                 padx="8px", height=1, font=("sans-serif", 16))
        self.inputProduto.grid(row=0, column=1)

        labelQuantidade = Label(self.view, text="Quantidade para reabastecer estoque: ",
                                font=("sans-serif", 16))
        labelQuantidade.grid(row=1, column=0)

        self.inputQuantidade = Text(self.view, width=60, pady="8px",
                                    padx="8px", height=1, font=("sans-serif", 16))
        self.inputQuantidade.grid(row=1, column=1)

        button1 = Button(self.view, text="reabastecer",
                         command=self.restockProduct, bg="orange", fg="white", pady="10px")
        button1.grid(column=11, row=9)

        self.view.mainloop()

        '''tela com os inputs para que se possa adicionar um produto'''

    def adicionarNovoProduto(self):
        self.view = Tk()
        self.view.title("Adicionar Produto")

        largura = 1280
        altura = 720

        largura_screen = self.view.winfo_screenwidth()
        altura_screen = self.view.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        self.view.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.view.iconbitmap("assets/images/shopping-cart-icon.ico")

        labelNome = Label(self.view, text="Nome do produto: ",
                          font=("sans-serif", 16))
        labelNome.grid(row=0, column=0)

        self.inputNome = Text(self.view, width=60, pady="8px",
                              padx="8px", height=1, font=("sans-serif", 16))
        self.inputNome.grid(row=0, column=1)

        labelId = Label(self.view, text="Id do produto: ",
                        font=("sans-serif", 16))
        labelId.grid(row=1, column=0)

        self.inputId = Text(self.view, width=60, pady="8px",
                            padx="8px", height=1, font=("sans-serif", 16))
        self.inputId.grid(row=1, column=1)

        labelPreco = Label(
            self.view, text="Preço do produto: ", font=("sans-serif", 16))
        labelPreco.grid(row=2, column=0)

        self.inputPreco = Text(self.view, width=60, pady="8px",
                               padx="8px", height=1, font=("sans-serif", 16))
        self.inputPreco.grid(row=2, column=1)

        labelDataFab = Label(
            self.view, text="Data de fabricação do produto: ", font=("sans-serif", 16))
        labelDataFab.grid(row=3, column=0)

        self.inputDataFab = Text(self.view, width=60, pady="8px",
                                 padx="8px", height=1, font=("sans-serif", 16))
        self.inputDataFab.grid(row=3, column=1)

        labelDataVal = Label(
            self.view, text="Data de validade do produto: ", font=("sans-serif", 16))
        labelDataVal.grid(row=4, column=0)

        self.inputDataVal = Text(
            self.view, width=60, pady="8px", padx="8px", height=1, font=("sans-serif", 16))

        self.inputDataVal.grid(row=4, column=1)

        self.labelQtdNoEstoque = Label(
            self.view, text="Quantidade no estoque: ", font=("sans-serif", 16))
        self.labelQtdNoEstoque.grid(row=5, column=0)

        self.inputQtdNoEstoque = Text(self.view, width=60, pady="8px",
                                      padx="8px", height=1, font=("sans-serif", 16))

        self.inputQtdNoEstoque.grid(row=5, column=1)
        self.button1 = Button(self.view, text="Adicionar", command=self.createNewProduct,
                              bg="orange", fg="white", pady="10px")
        self.button1.grid(column=10, row=7)

        self.view.mainloop()


produto1 = Produto(1, 'arroz', 2.50, '15/09/2024', '12/09/2022', 50)
produto2 = Produto(2, "Leite 1L", 5, "16/09/2022", "16/07/2022", 20)
produto3 = Produto(3, "Toddynho", 2.49, "16/09/2022", "16/07/2022", 20)
produto4 = Produto(4, 'feijao', 8.79, '05/02/2023', '10/10/2022', 120)
produto5 = Produto(5, 'sal', 0.79, '05/02/2023', '05/02/2022', 45)
produto6 = Produto(6, 'Cuscuz', 2.65, '18/11/2021', '10/06/2022', 80)

item1 = Item(produto1, 10)
item2 = Item(produto2, 3)
item3 = Item(produto3, 4)
item4 = Item(produto4, 12)
item5 = Item(produto5, 7)
item6 = Item(produto6, 1)
print("----------------------------ESTOQUE TESTE----------------------------\n")
estoque = Estoque()
estoque.adicionarNovoProduto(produto1)
print(estoque)
estoque.adicionarNovoProduto(produto2)
estoque.adicionarNovoProduto(produto3)
estoque.adicionarNovoProduto(produto4)
estoque.adicionarNovoProduto(produto5)
estoque.adicionarNovoProduto(produto6)
print(estoque)

estoque.reabastecerEstoque(produto2, 13)
print(estoque)


janela = Tk()
Main(janela)
janela.mainloop()
