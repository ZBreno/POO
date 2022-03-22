class Estoque:
    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos, 
    produtos é inicialmente instanciado como uma lista vazia, posteriormente os produtos
    serão adicionados"""
    def __init__(self, produtos=[]):
        self.__produtos = produtos

    """Metodo para facilitar e organizar exibição dos dados"""
    def __str__(self):
        return "\n\nProdutos: {}".format(" ".join(map(str, self.__produtos)))

    """Atravez desse metodo, novas instancias de produtos criadas são adicionadas
    na lista do estoque"""
    def adicionarNovoProduto(self, produto):
        self.__produtos.append(produto)

    """Atravez desse metodo, as instancias de produto são removidas do catalogo"""
    def removerProduto(self, produto):
        self.__produtos.remove(produto)

    """Get, para caso o uso seja necessario"""
    def get_produtos(self):
        return self.__produtos

    """Metodo aplicado apenas em quantidades, nele, o atributo de produto que 
    informa a quantidade de tal no estoque é acrescido"""
    def reabastecerEstoque(self, produto, quantidade):
        for i in range(len(self.__produtos)):
            if(produto == self.__produtos[i]):
                produto.set_quantidade_estoque(
                    produto.get_quantidade_estoque() + int(quantidade))
    
    """Usado apenas na hora de criar a interface com o TKInter"""
    def get_instancia(self, id):
        cont =0
        for i in range(len(self.__produtos)):
            cont +=1
            if(id == self.__produtos[i].get_id()):
                return self.__produtos[i]
            elif(cont == len(self.__produtos)):
                return 0
#comentario