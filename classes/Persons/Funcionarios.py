from datetime import datetime
from abc import ABC, abstractmethod
from classes.Finances.Compra import Compra
from classes.Finances.Conta import Conta
from classes.Produtcs.Item import Item
from classes.Produtcs.Produto import Produto

from colorama import Fore, Style
"""Classe mae, todas as variaçoes de funcionarios herdarão dela"""


class Funcionario(ABC):

    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos, endereço e contrato recebem instancias
    das classes com tal nome"""

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__sexo = sexo
        self.__contrato = contrato

    """Metodo abstrato, esse metodo será reescrito em cada uma das classes filha
    ja que o calculo realizado varia para cada tipo de funcionario"""
    @abstractmethod
    def calculo_previdencia_social(self):
        print(f"Imposto a ser pago com base no seu salário: R$ {7.5*1100/100}")

    """"Gets e sets, para caso o uso seja necessario"""

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def get_sexo(self):
        return self.__sexo

    def get_contrato(self):
        return self.__contrato

    def set_id(self, novo_id):
        self.__id = novo_id

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    def set_sexo(self, novo_sexo):
        self.__sexo = novo_sexo

    def set_contrato(self, novo_contrato):
        self.__contrato = novo_contrato


""""Classe filha, herdando de funcionario, recebe todos os atributos da classe mae"""


class Atendente(Funcionario):

    """Os atributos herdados são passados no metodo construtor, alem 
    de um atributo proprio dessa classe"""

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        """aributos herdados"""
        Funcionario.__init__(self, id, nome, cpf, endereco, sexo, contrato)
        self.__contrato = contrato
        self.__compras_realizadas = {}

    """Metodo reescrito"""

    def calculo_previdencia_social(self):
        print(f"Imposto a ser pago com base no seu salário: R$ {7.5*self.__contrato.get_salario()/100}\n")

    def comprovante_de_pagamento(self):
        caracteres = (34-len(" Lista de produtos "))*"="
        print(Fore.YELLOW+Style.BRIGHT+f"{caracteres}x Lista de Produtos x{caracteres}")
        print()

        produto2 = Produto(2, "sal", 5, "16/09/2022", "16/07/2022", 20)
        produto3 = Produto(3, "Toddynho", 2.49, "16/09/2022", "16/07/2022", 20)
        produto4 = Produto(4, 'feijao', 8.7, '05/02/2023', '10/10/2022', 120)
        produto5 = Produto(5, 'sal', 0.79, '05/02/2023', '05/02/2022', 45)
        produto6 = Produto(6, 'Cuscuz', 2.65, '18/11/2021', '10/06/2022', 80)

        item2 = Item(produto2, 3)
        item3 = Item(produto3, 4)
        item4 = Item(produto4, 12)
        item5 = Item(produto5, 7)
        item6 = Item(produto6, 1)

        compra = Compra(1, "add_na_conta", 0)
        compra.adicionar_item_na_lista(item2)
        compra.adicionar_item_na_lista(item3)
        compra.adicionar_item_na_lista(item4)
        compra.adicionar_item_na_lista(item5)
        compra.adicionar_item_na_lista(item6)

        caracteresIniciais = (48-len("NomePreço  Qntd"))*" "
        print(f"Nome{caracteresIniciais}Qntd  Preço")
        for x in compra.get_lista_itens():
            produto = x.get_produto()
            # espaco = len(str(x.get_quantidade()))
            caracteres = (len(produto.get_nome())+len(str("%.2f" % produto.get_preco()))+len(str(x.get_quantidade()))+len("R$ "))
            caracteres = (48-caracteres)*"."
            print(Fore.YELLOW+"{}{}{}  R$ {}".format(produto.get_nome(), caracteres, x.get_quantidade(
            ), str("%.2f" % produto.get_preco()).replace(".", ",")))

        print()
        print(50*"=")

        caracteres = len("Valor total{}R$ ".format("%.2f" % compra.get_valor_total()))
        caracteres = (50-caracteres)*"."
        
        print(Fore.YELLOW + Style.BRIGHT + "Valor total{}R$ {}".format(caracteres,str("%.2f" % compra.get_valor_total()).replace(".", ",")))
        

    '''Metodo onde o atendente recebe um valor do cliente, verifica se e suficiente, da troco caso necesssario e informa quanto de debito ficou restante'''
    def pagar_conta(self, conta, valor):
        conta.set_data_ultimo_pagamento(datetime.now())

        if valor <= conta.get_valor_a_pagar():
            conta.set_valor_a_pagar(conta.get_valor_a_pagar() - valor)
            print("Pagamento realizado\n")
        else:
            conta.set__valor_a_pagar(0)
            print("Conta paga! Troco de R$" +
                  valor - conta.get__valor_a_pagar())

    """Atraves desse metodo, as compras sao efetuadas, elas sao adicionadas no 
    resgistro de compras realizadas, o processo de pagamento é realizado, com 
    base no metodo de pagamento da compra e os dados que envolvem a realização 
    de compras são atualizados"""

    def registrarCompra(self, compra, conta, valor=None):
        conta.set_data_ultima_compra(datetime.now())

        if compra.get_metodoPagamento() == "add_na_conta":
            historico_conta = []
            if self.__compras_realizadas.get(conta) != None:
                historico_conta = self.__compras_realizadas[conta]

            historico_conta.append(compra)
            conta.set_valor_a_pagar(
                conta.get_valor_a_pagar() + compra.get_valor_total())

            self.__compras_realizadas[conta] = historico_conta
        elif compra.get_metodoPagamento() == "Especie":
            if compra.get_valor_total() == valor:
                print("Pagamento realizado, obrigado pela preferência")
            elif compra.get_valor_total() < valor:
                print(
                    f"Pagamento insuficiente. O valor da compra é R$ {compra.get_valor_total()}")
            else:
                print(
                    f"Pagamento realizado. Seu troco é de R$ {valor - compra.get_valor_total()}")
        else:
            print(
                f"O pagamento de R$ {compra.get_valor_total()} foi realizado com sucesso.\n")

        print("Compra registrada")
        for x in self.__compras_realizadas[conta]:
            print(x)


""""Classe filha, herdando de funcionario, recebe todos os atributos da classe mae"""


class Entregador(Funcionario):

    """Os atributos herdados são passados no metodo construtor"""

    def __init__(self, id, nome, cpf, endereco, sexo, contrato):
        Funcionario.__init__(self, id, nome, cpf, endereco, sexo, contrato)

    """Metodo sobrescrito"""

    def calculo_previdencia_social(self):
        print(
            f"Imposto a ser pago com base no seu salário: R$ {9.5*self.__contrato.get_salario()/100}")

    """Metodo onde a entrega dos produtos comprados é realizada, para isso, sao 
    forcecidos os dados da compra, ainda nesse metodo o frete da entrega é calculado"""

    def iniciar_entrega(self, compra, pagamento=None):
        print("Entrega sendo realizada para o endereço: ")
        print(compra.get_cliente().get_endereco())

        if (compra.get_valor_total() >= 100):
            print(
                "Como o valor da compra foi acima de R$ 100,00, você não precisa pagar uma taxa de entrega.")
        else:
            if pagamento == 15:
                print("Entrega em progresso")
            elif pagamento > 15:
                print("Entrega em progresso!\nTroco de R$" + pagamento - 15)
            else:
                print("O valor a ser pago deve ser de R$15.00")
