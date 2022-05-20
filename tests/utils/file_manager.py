import csv


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
