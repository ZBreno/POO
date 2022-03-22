class Compra:

    """Metodo costrutor: criando os atributos da classe, atributo lista de itens recebe instancias de classe Item 
    o valor total da compra sempre inicia zerada e cresce conforme os itens são adicionados"""
    def __init__(self, id, metodoPagamento, valor_total=0, lista_itens=[]):
        self.__id = id
        self.__valor_total = valor_total
        self.__metodoPagamento = metodoPagamento
        self.__lista_itens = []

    """Metodo para faciitar e organizar exibição dos dados da classe"""
    def __str__(self):
        return "\n---------------------------------\n➔ Valor total: {}\n➔ Metodo de Pagamento: {} \n\n➔ Lista dos itens na compra: {}\n---------------------------------".format(self.__valor_total, self.__metodoPagamento, " ".join(map(str, self.__lista_itens)))


    def adicionar_item_na_lista(self, item):
        if item.get_quantidade() <= item.get_produto().get_quantidade_estoque():
            self.__lista_itens.append(item)
            item.get_produto().set_quantidade_estoque(
                item.get_produto().get_quantidade_estoque() - item.get_quantidade())
            self.__valor_total += item.get_produto().get_preco() * item.get_quantidade()
        else:
            print("Quantidade insuficiente no estoque!")

    def remover_item_da_lista(self, item):
        self.__lista_itens.remove(item)
        item.get_produto().set_quantidade_estoque(
            item.get_produto().get_quantidade_estoque() + item.get_quantidade())
        self.__valor_total -= item.get_produto().get_preco() * item.get_quantidade()

    """"Gets e sets, para caso o uso seja necessario"""
    # GETS
    def get_id(self):
        return self.__id

    def get_lista_itens(self):
        return self.__lista_itens

    def get_valor_total(self):
        return self.__valor_total

    def get_metodoPagamento(self):
        return self.__metodoPagamento

    # SETS
    def set_id(self, id):
        self.__id = id

    def set_lista_itens(self, lista_itens):
        self.__lista_itens = lista_itens

    def set_metodoPagamento(self, metodoPagamento):
        self.__metodoPagamento = metodoPagamento
        print("Metodo de pagamento alterado!")

    def set_valor_total(self, valor_total):
        self.__valor_total = valor_total
