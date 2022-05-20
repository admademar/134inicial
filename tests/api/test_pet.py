# - Bibliotecas
import json

import pytest
import requests
# - Variaveis Publicas
from tests.utils.file_manager import ler_csv

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


def teste_excluir_pet():

    #Configura
    # Dados de Entrada
    pet_id = '9191910'

    #Resultado Esperado
    status_code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperado = '9191910'

    #Executa
    resultado_obtido = requests.delete(
        url=url + '/' + pet_id,
        headers=headers,

    )

    #Validar
    print(resultado_obtido)
    corpo_do_resulatdo_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resulatdo_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resulatdo_obtido['code'] == status_code_esperado
    assert corpo_do_resulatdo_obtido['type'] == type_esperado
    assert corpo_do_resulatdo_obtido['message'] == mensagem_esperado

@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status',
     ler_csv('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\vendors\\csv\\massa_incluir_pet.csv')
)
def teste_incluir_pet_em_massa(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status):

    corpo_json = '{'
    corpo_json += f' "id": {pet_id},'
    corpo_json += '"category": {'
    corpo_json += f'"id": {category_id},'
    corpo_json += f'"name": "{category_name}"'
    corpo_json += '},'
    corpo_json += f'"name": "{pet_name}",'
    corpo_json += '"photoUrls": ['
    corpo_json += ' "string"'
    corpo_json += '],'
    corpo_json += '"tags": ['
    corpo_json += '  {'
    corpo_json += f' "id": {tags_id},'
    corpo_json += f'"name": "{tags_name}"'
    corpo_json += ' }'
    corpo_json += '],'
    corpo_json += f' "status": "{status}"'
    corpo_json += '}'

    status_code_esperado = 200

    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name