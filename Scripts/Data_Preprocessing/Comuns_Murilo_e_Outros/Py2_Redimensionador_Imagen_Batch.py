# ## Múltiplas Imagens - Conversão de Formato
from PIL import Image
import os


def redimensionar_imagens_diretorio(pasta_origem, pasta_destino, tamanho=(300, 300)):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for nome_arquivo in os.listdir(pasta_origem):
        if nome_arquivo.lower().endswith(
            (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
        ):
            caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
            with Image.open(caminho_arquivo) as img:
                img.thumbnail(tamanho)  # Mantém a proporção
                img.convert("RGB").save(
                    os.path.join(pasta_destino, nome_arquivo)
                )  # Convertendo para RGB antes de salvar


# Redimensiona todas as imagens de pastas específicas
redimensionar_imagens_diretorio(
    r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pre_Pipeline\Murilo_Original_Bruto",
    r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Murilo\S1_Redimensionamento",
)

redimensionar_imagens_diretorio(
    r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pre_Pipeline\Outros_Sintetico_Bruto",
    r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Outros\S1_Redimensionamento",
)
