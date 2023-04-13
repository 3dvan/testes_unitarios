from codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '11/08/1998', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()