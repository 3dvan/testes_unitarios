from codigo.bytebank import Funcionario


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

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        salario: 100000 #given
        entrada_nome = 'João Yamato'
        esperado: 90000

        funcionario_teste = Funcionario('Teste', '11/08/1998', salario)
        funcionario_teste.decrescimo_salario()   #when
        resultado = funcionario_teste.salario

        assert resultado == esperado