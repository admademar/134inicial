# ToDo: - 3 Criar uma venda de um Pet para um Usuário
# ToDo: - 4 Consultar os dados do Pet que foi vendido
import json

import requests
url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}

def teste_vernder_pet():
    # - Configura
    # Dados de Entrada virão do pedido1.json

    # Resultado esperado
    status_code_esperado = 200
    pedido_id_esperado = 55551
    pet_id_esperado = 9191910
    status_pedido_esperado = 'placed'

    # - Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\vendors\\json\\pedido1.json')
    )
    # - Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_resultado_obtido['status'] == status_pedido_esperado

