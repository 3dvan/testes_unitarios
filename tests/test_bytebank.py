from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_11_08_1998_deve_retornar_25(self):
        entrada = '11/08/1998'  # Given-contexto
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        #When-Ação
        resultado = funcionario_teste.idade()

        assert resultado == esperado #Then-desfecho

    def test_quando_sobrenome_recebe_Manoel_Edvan_deve_retornar_Carvalho(self):
        entrada = 'Manoel Edvan'
        esperado = 'Edvan'

        edvan = Funcionario(entrada, '11/08/1998', 2000)
        resultado = edvan.sobrenome()

        assert resultado == esperado


    #@mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funconario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funconario_teste.decrescimo_salario()  # when
        resultado = funconario_teste.salario

        assert resultado == esperado  # then


    #@mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000  # given
        entrada_nome = 'Ana'
        esperado = 100

        funconario_teste = Funcionario(entrada_nome, '11/02/1998', entrada_salario)
        resultado = funconario_teste.calcular_bonus() #when

        assert resultado == esperado  # then

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000  # given

            funconario_teste = Funcionario('teste', '11/02/1998', entrada_salario)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado
