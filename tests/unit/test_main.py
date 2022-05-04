from main import somar, subtrair, multiplicar, dividir

def teste_somar():
    # 1 - Configura
    numero_a = 7
    numero_b = 13
    resultado_esperado = 20

    # 2 - Executa

    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido

def teste_subtrair():
    # 1 - Configura
    numero_a = 15
    numero_b = 10
    resultado_esperado = 5

    # 2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido

def teste_multiplicar():
    # 1 - Configurar
    numero_a = 25
    numero_b = 25
    resultado_esperado = 625

    # 2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido

def teste_dividir_positivo():
    # 1 - Preparar/Configurar
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 3

    # 1.2 - Resultados Esperados
    resultado_esperado = 9

    # 2 - Executar
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Validar
    assert resultado_obtido == resultado_esperado


def teste_dividir_negativo():
    # 1 - Preparar/Configurar
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 0

    # 1.2 - Resultados Esperados
    resultado_esperado = 'Não dividiras por Zero'

    # 2 - Executar
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Validar
    assert resultado_obtido == resultado_esperado