# Done: - 1 Criar um teste que adicione um Usuário
# Done: - 2 Realizar o login e extrair o token da resposta
# Done: - 3 Criar uma venda de um Pet para um Usuário
# Done: - 4 Consultar os dados do Pet que foi vendido
import json

import requests
url = 'https://petstore.swagger.io/v2/user'

headers = {'Content-Type': 'application/json'}
token = ''

def test_incluir_usuario():

    # - 1 Configura
    # Dados de Entrada, Virão do arquivo usuario1.json


    # Resultados Esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagen_esperado = '44441'


    # - 2 Executar

    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\vendors\\json\\usuario1.json')
    )
    # - 3 Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagen_esperado

def test_login():

    # Configura
    # Dados de Entrada

    username = 'Herry'
    password = 'dunha'

    # Resultados Esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagen_esperado = '44441'

    #Executa
    resulatdo_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers,

    )
    #Valida

    print(resulatdo_obtido)
    corpo_do_resultado_obtido = resulatdo_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resulatdo_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagen_esperado.find(corpo_do_resultado_obtido['message'])


    # - Extari

    mensagen_extraida = corpo_do_resultado_obtido.get('message')
    print(f'A messagen = {mensagen_extraida}')
    token = mensagen_extraida[23:]  #[inicio:fim]
    print(f' O Token = {token}')




