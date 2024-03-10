import os
from PIL import Image, ImageEnhance, ImageOps, ImageFilter


def augmentar_imagens(diretorio_origem):
    # Define o caminho do diretório onde as imagens augmentadas serão salvas
    diretorio_destino = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Murilo\S4_Argumentacao"

    # Cria o diretório de destino se ele não existir
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Processa cada arquivo no diretório de origem
    for arquivo in sorted(os.listdir(diretorio_origem)):
        if arquivo.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            caminho_arquivo_origem = os.path.join(diretorio_origem, arquivo)
            imagem = Image.open(caminho_arquivo_origem)
            nome_arquivo, extensao = os.path.splitext(arquivo)

            # Identifica a próxima numeração de argumentação baseada nas imagens existentes no diretório destino
            maior_numero_augmentacao = (
                9  # Inicia a contagem de onde as outras argumentações terminaram
            )
            for arg in os.listdir(diretorio_destino):
                if (
                    arg.startswith(nome_arquivo)
                    and arg.endswith(extensao)
                    and "_A" in arg
                ):
                    numero_augmentacao = int(arg.split("_A")[-1].split(".")[0])
                    if numero_augmentacao > maior_numero_augmentacao:
                        maior_numero_augmentacao = numero_augmentacao

            # Adiciona blur à imagem original e salva com a numeração correta para A10
            imagem_blur = imagem.filter(ImageFilter.BLUR)
            imagem_blur.save(
                os.path.join(
                    diretorio_destino,
                    f"{nome_arquivo}_A{maior_numero_augmentacao+1}{extensao}",
                )
            )

            # Continua com as outras argumentações normalmente
            # Cria as variações de luminosidade, excluindo A2 e A3
            fatores = [1.75, 0.45]  # Ajuste para remover A2 e A3 e manter A1 e A4
            for i, fator in enumerate(fatores):
                melhorador = ImageEnhance.Brightness(imagem)
                imagem_melhorada = melhorador.enhance(fator)
                # Salva como A1 e A2 porque estamos pulando A2 e A3 originais
                imagem_melhorada.save(
                    os.path.join(diretorio_destino, f"{nome_arquivo}_A{i+1}{extensao}")
                )

            # Espelha a imagem
            imagem_espelhada = ImageOps.mirror(imagem)
            imagem_espelhada.save(
                os.path.join(diretorio_destino, f"{nome_arquivo}_A3{extensao}")
            )

            # Converte para preto e branco
            imagem_pb = imagem.convert("L")
            imagem_pb.save(
                os.path.join(diretorio_destino, f"{nome_arquivo}_A4{extensao}")
            )

            # Cria rotações de imagem
            for i, angulo in enumerate([90, 180, 270]):  # ângulos para rotação
                imagem_rotacionada = imagem.rotate(angulo)
                imagem_rotacionada.save(
                    os.path.join(diretorio_destino, f"{nome_arquivo}_A{5+i}{extensao}")
                )

            # Zoom in (corta a imagem para dar efeito de aproximação)
            largura, altura = imagem.size
            zoom_in = imagem.crop(
                (largura * 0.2, altura * 0.2, largura * 0.8, altura * 0.8)
            )
            zoom_in.save(
                os.path.join(diretorio_destino, f"{nome_arquivo}_A8{extensao}")
            )

            # Zoom out (adiciona borda para dar efeito de afastamento)
            zoom_out = ImageOps.expand(imagem, border=int(largura * 0.2), fill="black")
            zoom_out.save(
                os.path.join(diretorio_destino, f"{nome_arquivo}_A9{extensao}")
            )


# Caminho para a pasta com as imagens originais
diretorio_imagens_originais = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Murilo\S3_Renomeamento_Original"

# Chama a função para aplicar augmentação nas fotos
augmentar_imagens(diretorio_imagens_originais)


import os
from PIL import Image, ImageEnhance, ImageOps, ImageFilter


def adicionar_argumentacao_color(diretorio_origem, diretorio_destino):
    # Verifica se o diretório de destino existe, se não, cria
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Contador para limitar a aplicação da argumentação color às primeiras 16 imagens
    contador = 0

    # Processa cada arquivo no diretório de origem
    for arquivo in sorted(os.listdir(diretorio_origem)):
        # Limita a argumentação color às primeiras 16 imagens originais
        if contador >= 16:
            break

        if arquivo.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            caminho_arquivo_origem = os.path.join(diretorio_origem, arquivo)
            imagem = Image.open(caminho_arquivo_origem)
            nome_arquivo, extensao = os.path.splitext(arquivo)

            # Identifica a última numeração de argumentação para continuar a sequência
            maior_numero_augmentacao = 0
            for arg in os.listdir(diretorio_destino):
                if (
                    arg.startswith(nome_arquivo)
                    and arg.endswith(extensao)
                    and "_A" in arg
                ):
                    numero_augmentacao = int(arg.split("_A")[-1].split(".")[0])
                    maior_numero_augmentacao = max(
                        maior_numero_augmentacao, numero_augmentacao
                    )

            # Aplica argumentação de cor 0.5
            melhorador_cor = ImageEnhance.Color(imagem)
            imagem_color = melhorador_cor.enhance(0.5)
            # Salva a imagem argumentada com a numeração correta
            imagem_color.save(
                os.path.join(
                    diretorio_destino,
                    f"{nome_arquivo}_A{maior_numero_augmentacao+1}{extensao}",
                )
            )

            # Incrementa o contador após processar uma imagem
            contador += 1


# Define os caminhos para os diretórios de imagens originais e imagens argumentadas
diretorio_imagens_originais = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Murilo\S3_Renomeamento_Original"
diretorio_imagens_argumentadas = r"C:\Users\User\OneDrive\Desktop\AssistenteSeguro_FreioAntiColisao\Datasets\Pipeline\Murilo\S4_Argumentacao"

# Chama a função para adicionar argumentação color às primeiras 16 imagens originais
adicionar_argumentacao_color(
    diretorio_imagens_originais, diretorio_imagens_argumentadas
)
