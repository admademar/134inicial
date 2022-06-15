# ToDo: - 3 Criar uma venda de um Pet para um Usuário
# ToDo: - 4 Consultar os dados do Pet que foi vendido
import json
import os.path

import requests
url = 'https://petstore.swagger.io/v2/'
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
    caminho = os.path.abspath(__file__ + "/../../../") + os.sep + 'vendors' + os.sep+'json'+ os.sep

    resultado_obtido = requests.post(
        url=url + 'store/order',
        headers=headers,
        data=open(caminho + 'pedido1.json')
      )
    # - Valida
    print(resultado_obtido)
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_resultado_obtido['status'] == status_pedido_esperado

    #Extrai
    pet_id_extraido = corpo_resultado_obtido.get('petId')

    #Realizar a 2ª Transação

    #Configura
    #Configura
    #Dados de Entrada
    #Extraido da 1ª transação acima

    #Resulatado Esperado
    pet_name_esperado = 'Dolly2'
    status_code_esperado = 200

    #Executa
    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    #Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_resultado_obtido, indent= 4 ))
    assert corpo_resultado_obtido['name'] == pet_name_esperado

