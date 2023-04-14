from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_11_08_1998_deve_retornar_25(self):
        entrada = '11/08/1998'  # Given-contexto
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        #When-Ação
        resultado = funcionario_teste.idade()

        assert resultado == esperado #Then-desfecho
