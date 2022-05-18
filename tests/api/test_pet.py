# - Bibliotecas
import json

import pytest
import requests
# - Variaveis Publicas
url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}

# - Definições/Funcões(Defs)

def teste_incluir_pet():


    # - Configura/Preparar / Dados de Entrada(pet1.json)


    # - Resultados Esperados

    status_code_esperado = 200
    pet_id_esperado = 9191910
    pet_nome_esperado = "Dolly2"
    pet_nome_categoria_esperado = "Cachorro"
    pet_nome_tag_esperado = "vacinado"


    # - Executa

    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\vendors\\json\\pet1.json')
    )


   # - Valida/Check

    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


def teste_consultar_pet():


    # Configurar/Preparar
    # Dados de Entrada (petid)

    pet_id = '9191910'

    # - Resultados Esperados

    status_code_esperado = 200
    pet_id_esperado = 9191910
    pet_nome_esperado = "Dolly2"
    pet_nome_categoria_esperado = "Cachorro"
    pet_nome_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers,
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


def teste_alterar_pet():

    #Configurar/Preparar
    #Dados de Entrada virão do (pet2.json)


    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 9191910
    pet_nome_esperado = "Dolly2"
    pet_nome_categoria_espeardo = "Cachorro"
    pet_name_tag_esperado ="vacinado"
    pet_status_esperado = "pending"


    # Executa

    resultado_obtido = requests.put(

        url=url,
        headers=headers,
        data=open('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\vendors\\json\\pet2.json')
    )

    #Valida

    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_espeardo
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_name_tag_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado




