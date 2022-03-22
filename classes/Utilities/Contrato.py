from datetime import datetime
class Contrato:
    """Metodo costrutor: criando os atributos da classe e inicializando os mesmos"""
    def __init__(self, id, data_inicio, data_fim, salario, horario_entrada, horario_saida,carga_horaria):
        self.__id = id
        self.__data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        self.__data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()
        self.__salario = salario
        self.__horario_entrada = datetime.strptime(horario_entrada, '%H/%M').date()
        self.__horario_saida = datetime.strptime(horario_saida, '%H/%M').date()
    
    """Metodo para facilitar e organizar exibição dos dados"""
    def __str__(self):
        return "------Contrato Individual de trabalho------\n\nID do contrato: {self.__id}\nData de inicio: {self.__data_inicio}\nData de finalização: {self.__data_fim}\nSalario: {self.__salario}\nHorario de inicio do expediente: {self.__horario_entrada}\nHorario de fim do expediente: {self.__horario_saida}"

    """"Gets e sets, para caso o uso seja necessario"""
    def get_id(self):
        return self.__id

    def get_data_inicio(self):
        return self.__data_inicio

    def get_data_fim(self):
        return self.__data_fim

    def get_salario(self):
        return self.__salario

    def get_horario_entrada(self):
        return self.__horario_entrada

    def get_horario_saida(self):
        return self.__horario_saida

    def set_id(self, id):
        self.__id = id

    def set_data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    def set_data_fim(self, data_fim):
        self.__data_fim = data_fim

    def set_salario(self, salario):
        self.__salario = salario

    def set_horario_entrada(self, horario_entrada):
        self.__horario_entrada = horario_entrada

    def set_horario_saida(self, horario_saida):
        self.__horario_saida = horario_saida