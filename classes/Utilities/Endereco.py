class Endereco:
    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos, dados de localização"""
    def __init__(self, rua, numero, bairro, cep, cidade, estado):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado

    """Metodo para facilitar e organizar exibição dos dados"""
    def __str__(self):
        # return "Rua: {} \nNúmero: {} \nBairro: {} \nCEP: {} \nCidade: {} \nEstado: {}".format(self.__rua, self.__numero, self.__bairro, self.__cep, self.__cidade, self.__estado)
        return f"{self.__rua}, {self.__bairro}, {self.__numero} | {self.__cep}, {self.__cidade}-{self.__estado.upper()}"

    """"Gets e sets, para caso o uso seja necessario"""
    def get_rua(self):
        return self.__rua

    def get_numero(self):
        return self.__numero

    def get_bairro(self):
        return self.__bairro

    def get_cep(self):
        return self.__cep

    def get_cidade(self):
        return self.__cidade

    def get_estado(self):
        return self.__estado

    def set_rua(self, nova_rua):
        self.__rua = nova_rua

    def set_numero(self, novo_numero):
        self.__numero = novo_numero

    def set_bairro(self, novo_bairro):
        self.__bairro = novo_bairro

    def set_cep(self, novo_cep):
        self.__cep = novo_cep

    def set_cidade(self, novo_cidade):
        self.__cidade = novo_cidade

    def set_estado(self, novo_estado):
        self.__estado = novo_estado
