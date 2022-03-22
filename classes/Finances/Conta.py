from datetime import datetime
'''Classe criada para o cliente deixar sua compra em debito para depois pagar'''
class Conta:

    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos, titular recebe uma instancia
    se cliente, data do ultimo pagamento e da ultima compra sao atualizadas quando a compra é realizada pelo
    atendente"""
    def __init__(self, titular, valor_a_pagar):
        self.__titular = titular
        self.__valor_a_pagar = valor_a_pagar
        self.__data_ultimo_pagamento = "Cliente não fez nenhum pagamento"
        self.__data_ultima_compra = "Cliente não fez nenhuma compra"

    '''Metodo para faciitar e organizar exibição dos dados da classe '''
    def __str__(self):
        return "Titular: {} \nValor a pagar: {} \nData de ultimo pagamento: {} \nData de ultima compra: {}".format(self.__titular, self.__valor_a_pagar, self.__data_ultimo_pagamento, self.__data_ultima_compra)

    """"Gets e sets, para pegar os valores dos atributos ou altera-los, caso seja necessario"""
    def get_titular(self):
        return self.__titular

    def get_valor_a_pagar(self):
        return self.__valor_a_pagar

    def get_data_ultimo_pagamento(self):
        return self.__data_ultimo_pagamento

    def get_data_ultima_compra(self):
        return self.__data_ultima_compra

    def set_titular(self, nova_titular):
        self.__titular = nova_titular

    def set_valor_a_pagar(self, nova_valor_a_pagar):
        self.__valor_a_pagar = nova_valor_a_pagar

    def set_data_ultimo_pagamento(self, nova_data_ultimo_pagamento):
        self.__data_ultimo_pagamento = nova_data_ultimo_pagamento

    def set_data_ultima_compra(self, nova_data_ultima_compra):
        self.__data_ultima_compra = nova_data_ultima_compra
