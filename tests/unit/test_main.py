import csv

import pytest

from main import somar, subtrair, multiplicar, dividir


def ler_csv(arquivo_csv):
    # Criamos uma folha em Branco
    dados_csv =[]
    try:  # Abrimos o arquivos
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não Encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


def teste_somar():
    # 1 - Configura
    numero_a = 7
    numero_b = 8
    resultado_esperado = 15

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
@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\vendors\\csv\\massa_teste_subtrair_positivo.csv'))
def teste_subtrair_leitura_csv(numero_a, numero_b, resultado_esperado):
        # 1 - Configura

        # 2 - Executa
        resultado_obtido = subtrair(int(numero_a), int(numero_b))

        # 3 - Valida
        assert resultado_obtido == int(resultado_esperado)


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


# lista para uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado, ):
    # 1 - Configura
    # utilizamos a lista como massa de teste
    # massa de dodos para a função somar

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',ler_csv('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\vendors\\csv\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado,):
    # 1 - Configura
    # utilizamos a lista como massa de teste
    # massa de dodos para a função somar

    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)
