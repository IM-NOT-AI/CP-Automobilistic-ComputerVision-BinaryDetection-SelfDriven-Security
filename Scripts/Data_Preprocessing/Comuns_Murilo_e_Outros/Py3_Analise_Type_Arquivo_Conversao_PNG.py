import os
import pandas as pd
from collections import Counter
from PIL import Image


# Função modificada para converter imagens e contar os tipos de arquivos
def converter_e_contar_arquivos(pasta_origem, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    extensoes = [
        ".jpg",
        ".jpeg",
        ".bmp",
        ".tif",
        ".tiff",
        ".gif",
        ".png",
        ".eps",
        ".raw",
    ]
    tipos_arquivos = []  # Lista para armazenar os tipos de arquivos encontrados

    for nome_arquivo in os.listdir(pasta_origem):
        if any(nome_arquivo.lower().endswith(ext) for ext in extensoes):
            try:
                imagem = Image.open(os.path.join(pasta_origem, nome_arquivo))
                nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]
                imagem.save(
                    os.path.join(pasta_destino, nome_arquivo_sem_extensao + ".png"),
                    "PNG",
                )
                tipos_arquivos.append(
                    os.path.splitext(nome_arquivo.lower())[1]
                )  # Adiciona o tipo do arquivo à lista
            except Exception as e:
                print(f"Não foi possível converter o arquivo {nome_arquivo}: {e}")

    # Retorna um contador com a quantidade de cada tipo de arquivo
    return Counter(tipos_arquivos)


# Função para criar DataFrames de contagem
def criar_dataframe_contagem(contagem):
    return pd.DataFrame(
        list(contagem.items()), columns=["Tipo de Arquivo", "Quantidade"]
    )


# Caminhos fornecidos para Murilo e Outros
pasta_origem_murilo = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Murilo\S1_Redimensionamento"
pasta_destino_murilo = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Murilo\S2_Conversao"

pasta_origem_outros = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Outros\S1_Redimensionamento"
pasta_destino_outros = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Outros\S2_Conversao"

# Contagem e conversão para Murilo e Outros
contagem_murilo = converter_e_contar_arquivos(pasta_origem_murilo, pasta_destino_murilo)
contagem_outros = converter_e_contar_arquivos(pasta_origem_outros, pasta_destino_outros)

# Criando DataFrames para cada conjunto
df_murilo = criar_dataframe_contagem(contagem_murilo)
df_outros = criar_dataframe_contagem(contagem_outros)

# Imprimindo os DataFrames
print("DataFrame para Murilo:")
print(df_murilo)
print("\nDataFrame para Outros:")
print(df_outros)
