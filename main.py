from classes.Persons.Cliente import Cliente
from classes.Finances.Compra import Compra
from classes.Finances.Conta import Conta
from classes.Utilities.Contrato import Contrato
from classes.Utilities.Endereco import Endereco
from classes.Produtcs.Estoque import Estoque
from classes.Persons.Funcionarios import Atendente, Entregador
from classes.Produtcs.Item import Item
from classes.Produtcs.Produto import Produto

import uuid
import os

produto2 = Produto(2, "Leite 1L", 5, "16/09/2022", "16/07/2022", 20)
produto3 = Produto(3, "Toddynho", 2.49, "16/09/2022", "16/07/2022", 20)
produto4 = Produto(4, 'feijao', 8.79, '05/02/2023', '10/10/2022', 120)
produto5 = Produto(5, 'sal', 0.79, '05/02/2023', '05/02/2022', 45)
produto6 = Produto(6, 'Cuscuz', 2.65, '18/11/2021', '10/06/2022', 80)


item2 = Item(produto2, 3)
item3 = Item(produto3, 4)
item4 = Item(produto4, 12)
item5 = Item(produto5, 7)
item6 = Item(produto6, 1)

estoque = Estoque()


estoque.reabastecerEstoque(produto2, 13)
contrato1 = Contrato(1, '12/09/2021', '12/09/2022',
                     1200.00, '08/00', '17/00', "08:00")
contrato2 = Contrato(2, '12/09/2021', '12/09/2023',
                     1500.00, '08/00', '17/00', "08:00")
endereco1 = Endereco("Rua Maria das Flores", "129",
                     "Centro", "599000-000", "Mossoro", "RN")
endereco2 = Endereco("Rua Maria das Flores", "129",
                     "Centro", "599000-000", "Mossoro", "RN")
atendente = Atendente(1, "Jose de Sousa", "123.456.789-01",
                      endereco1, "M", contrato1)
entregador = Entregador(
    2, "Felippe Rian", "012-345-678-90", endereco2, "M", contrato2)


escolha = int(input(
    "Escolhas: \n1 - Sou Atendente \n2 - Sou Entregador \n3 - Encerrar programa\n\nInforme a opção desejada: "))
os.system('cls' if os.name == 'nt' else 'clear')
lista_clientes = []
if __name__ == "__main__":

    while True:

        if(escolha == 1):

            escolha_atendente = int(input(
                "Oque deseja fazer? \n\n1 - Calcular previdencia Social \n2 - Pagamento de debito \n3 - Registrar Compra \n4 - Adicionar produto no estoque \n5 - Reabastecer produto no estoque \n6 - Remover produto do estoque \n7 - Cadastrar cliente \n8 - Listar clientes \n9 - Trocar Usuario \n0 - Sair do sistema \n\nEscolha: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if(escolha_atendente == 1):
                print("\nCalculando previdencia...")
                atendente.calculo_previdencia_social()
            elif(escolha_atendente == 2):
                cliente = input("\nA conta de qual cliente sera paga? ")
                valor = float(input("Quanto ele pretende pagar? "))
                atendente.pagar_conta(cliente.get_conta(), valor)

            elif(escolha_atendente == 3):

                cliente = input("\nInforme o ID do cliente que esta realizando a compra: ")
                for x in lista_clientes:
                    if x == cliente:
                        metodo = input(
                            "\nQual vai ser o metodo de pagamento da compra? \n\nadd_na_conta\nEspecie\netc...\n\nInforme:")
                        compra = Compra(uuid.uuid4(), metodo)
                        print("\nSelecionando itens da compra...\n")
                        while True:
                            print(estoque, "\n")
                            print(compra)
                            escolha_compra = int(input(
                                "\nAdicionar item na lista (1)\nRemover item da lista(2)\nFinalizar seleção de produtos(3)\n\nSelecione: "))

                            if escolha_compra == 1:
                                nome_produto = input("\nDigite o nome do produto: ")
                                quantidade = int(
                                    input("\nDigite a quantidade: "))
                                instancia = estoque.get_instancia(nome_produto)
                                item = Item(instancia, quantidade)

                                compra.adicionar_item_na_lista(item)
                            elif escolha_compra == 2:
                                x = int(
                                    input("Qual item deseja remover (1º, 2º, 3º...): "))
                                compra.remover_item_da_lista(
                                    compra.get_lista_itens[x-1])

                            elif escolha_compra == 3:
                                break
                            else:
                                print("Opção invalida")

                            atendente.registrarCompra(compra, x.get_conta())
                    else:
                        print("Esse cliente não esta cadastrado no sistema\n")

            elif(escolha_atendente == 4):
                print("Produto: ")
                nome_produto = input("Digite o nome do produto: ")
                preco_produto = float(input("Digite o preço do produto: "))
                data_validade_produto = input(
                    "Digite a data de validade do produto(dia/mes/ano): ")
                data_fabricacao_produto = input(
                    "Digite a data de fabricação do produto(dia/mes/ano): ")
                quantidade_produto = int(input("Digite a quantidade: "))
                produto = Produto(uuid.uuid4(), nome_produto, preco_produto,
                                  data_validade_produto, data_fabricacao_produto, quantidade_produto)
                estoque.adicionarNovoProduto(produto)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Seu produto foi adicionado com sucesso!\n\n")

            elif(escolha_atendente == 5):
                print(estoque)
                id_produto = int(input("Digite o id do produto: "))
                instancia = estoque.get_instancia(id_produto)
                quantidade_produto = int(input("Digite a quantidade: "))
                estoque.reabastecerEstoque(instancia, quantidade_produto)

            elif(escolha_atendente == 6):
                print(estoque)
                id_produto = int(input("Digite o id do produto: "))
                instancia = estoque.get_instancia(id_produto)
                estoque.removerProduto(instancia)

            elif(escolha_atendente == 7):
                nome_cliente = input("Digite o nome do cliente: ")
                data_nascimento_cliente = input(
                    "Digite a data de nascimento do cliente(YYYY-MM-DD): ")
                print(f"Endereço do {nome_cliente}: ")
                rua_cliente = input(
                    f"Digite o nome da rua do {nome_cliente}: ")
                numero_cliente = input(
                    f"Digite o número da casa do {nome_cliente}: ")
                bairro_cliente = input(
                    f"Digite o nome do bairro do {nome_cliente}: ")
                cep_cliente = input(
                    f"Digite o número do CEP do {nome_cliente}: ")
                cidade_cliente = input(f"Digite a cidade do {nome_cliente}: ")
                estado_cliente = input(
                    f"Digite o nome do estado do {nome_cliente}: ")
                endereco = Endereco(rua_cliente, numero_cliente, bairro_cliente,
                                    cep_cliente, cidade_cliente, estado_cliente)
                cliente = Cliente(uuid.uuid4(), nome_cliente,
                                  data_nascimento_cliente, endereco)
                lista_clientes.append(nome_cliente)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Cliente cadastrado com sucesso!")
                

            elif(escolha_atendente == 8):
                for i in range(len(lista_clientes)):
                    print(lista_clientes[i],"\n")

            elif(escolha_atendente == 9):
                escolha = 2
                break

            elif(escolha_atendente == 0):
                print("Desligando...")
                break
