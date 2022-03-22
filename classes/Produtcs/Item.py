"""Essa classe existe apenas para facilitar a geração de intancias de compra,
são instancias dele que são adicionadas na lista de itens da compra"""
class Item:

    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos, 
    produto recebe uma instancia de Produto e em outro atributo uma quantidade é passada, 
    para depois ser colocado em sua compra"""
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    """Metodo para facilitar e organizar exibição dos dados"""
    def __str__(self):
        return f"\n{self.__produto}  ↪ Quantidade: {self.__quantidade}"

    """"Gets e sets, para caso o uso seja necessario"""
    def get_produto(self):
        return self.__produto

    def get_quantidade(self):
        return self.__quantidade

    def set_produto(self, novo_produto):
        self.__produto = novo_produto

    def set_quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade