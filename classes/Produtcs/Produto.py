from datetime import datetime


class Produto:
    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos,
    caso nao informada, a quantidade no estoque e zerada"""

    def __init__(self, id, nome, preco, data_validade, data_fabricacao, quantidade_estoque=0):
        self.__id = id
        self.__nome = nome
        self.__preco = preco        
        self.__data_validade = datetime.strptime(data_validade, '%d/%m/%Y').date()
        self.__data_fabricacao = datetime.strptime(data_fabricacao, '%d/%m/%Y').date()
        self.__quantidade_estoque = quantidade_estoque

    """Metodo para facilitar e organizar exibição dos dados"""

    def __str__(self):
        return (f"\n  ↪ Produto: {self.__nome}\n  ↪ Id: {self.__id}\n  ↪ Preço: {self.__preco}\n  ↪ Data de validade: {self.__data_validade}\n  ↪ Data de fabricação: {self.__data_fabricacao}\n  ↪ Quantidade disponível no estoque: {self.__quantidade_estoque}\n")

    """"Gets e sets, para caso o uso seja necessario"""

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_data_validade(self):
        return self.__data_validade

    def get_data_fabricacao(self):
        return self.__data_fabricacao

    def get_quantidade_estoque(self):
        return self.__quantidade_estoque

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_data_validade(self, data_validade):
        self.__data_validade = data_validade

    def set_data_fabricacao(self, data_fabricacao):
        self.__data_fabricacao = data_fabricacao

    def set_quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

