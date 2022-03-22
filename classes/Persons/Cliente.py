from datetime import datetime
'''Classe criada para '''
class Cliente:
    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos, endereço recebe uma instancia de Endereco
    data de nascimento recebe uma string, mas a converte para o formato datetime"""
    def __init__(self, id, nome, data_nascimento, endereco):
        self.__id = id
        self.__nome = nome
        self.__data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        self.__endereco = endereco
        

    """Metodo para facilitar e organizar exibição dos dados"""
    def __str__(self):
        return "\nID do cliente: {} \nNome do cliente: {} \nData de Nascimento: {} \nEndereco: {}".format(self.__id, self.__nome, self.__data_nascimento, self.__endereco)

    """"Gets e sets, para pegar os valores dos atributos ou altera-los, caso seja necessario"""
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_endereco(self):
        return self.__endereco

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def set_endereco(self, endereco):
        self.__endereco = endereco
