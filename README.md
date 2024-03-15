# CP-Automobilistic-ComputerVision-BinaryDetection-SelfDriven-Security
Este repositório aborda a transformação de um Fusca dos anos 90 em veículo autônomo usando visão computacional, Detecção Binária, Robótica e IoT. Fornece datasets, scripts e macetes para treinamento do modelo. Contribuições para melhoria e expansão são bem-vindas. Confira a licença para detalhes de uso.


![ic_title_readme](https://github.com/IM-NOT-AI/CP-Automobilistic-ComputerVision-BinaryDetection-SelfDriven-Security/assets/113378671/90c7e4dc-8429-4f50-b234-9c5725ffa1ba)


<p align="center">
  <img src="https://github.com/IM-NOT-AI/CP-Automobilistic-ComputerVision-BinaryDetection-SelfDriven-Security/assets/113378671/d4245819-e8e5-4710-ba9d-4fa8513d49b5" alt="fusca_foto_ic" width="500">
</p>

<details>
  <summary><h2>🚗 DEMONSTRAÇÃO</h2></summary>
    
  <p align="center">
    <img src="https://github.com/IM-NOT-AI/CP-Automobilistic-ComputerVision-BinaryDetection-SelfDriven-Security/assets/113378671/3423ca03-691a-459f-a18f-772a95c1597e" alt="output" width="500">
  </p>

  <p>
  Este projeto demonstra um sistema inovador de detecção e reconhecimento automático utilizando visão computacional e aprendizado de máquina para identificar especificamente "Murilo" entre outros indivíduos. Utilizando uma câmera acoplada a um veículo (neste caso, um modelo simbólico como um "Fusca"), o sistema é capaz de discernir entre duas classes principais: "Murilo" e "Outros".

  A lógica do sistema é relativamente direta, mas altamente eficaz: ao detectar a presença de um indivíduo, ele classifica quem está à frente. Se "Murilo" for identificado dentro de um raio de 3 metros, o sistema ativa um mecanismo de controle mecânico que desengata a embreagem do veículo. Este processo é projetado para que, ao reconhecer "Murilo" a uma distância de até 3 metros, o carro automaticamente reduza sua velocidade ou pare, garantindo uma interação segura e controlada.

  O mecanismo por trás desse processo envolve o uso de técnicas avançadas de visão computacional com OpenCV para o processamento de imagens em tempo real e TensorFlow ou TFLite para o modelo de aprendizado de máquina que faz a distinção entre as classes. O controle do veículo é gerenciado por um sistema embarcado, como o Raspberry Pi, que se comunica com os componentes mecânicos para operar a embreagem com base na entrada do modelo de detecção.
  </p>
  
</details>

---

<details>
  <summary><h2>📘 UTILIZAÇÃO</h2></summary>
  <p align="center">
    <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/f2e975e4-44f2-48d3-b5f6-0b7dcfb61944" alt="pipeline-root" width="600" />
  </p>
  <br>
  <details>
    <summary><h3>01 - ENTENDIMENTO DO PROBLEMA</h3></summary>
    <p align="center">
      <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/1bee522f-4cec-424c-a663-d3d0714b3df2" alt="fusca_foto_ic" width="250">
    </p>
    O primeiro passo em direção ao desenvolvimento do projeto AssistenteSeguro FreioAntiColisão é o entendimento profundo do problema a ser resolvido. Este processo inicial é vital para a formulação de objetivos claros e a identificação das necessidades de dados, tecnologia e stakeholders envolvidos. A seguir, detalhamos os componentes essenciais desta fase: 
    <br><br>
    <details>
      <summary>📄 Definição do Objetivo</summary>
      O projeto, AssistenteSeguro FreioAntiColisão, é projetado para aumentar a segurança veicular desenvolvendo um sistema avançado de detecção capaz de identificar potenciais ameaças de colisão, focando especificamente em reconhecer "Murilo" e "Outros". Esta classificação binária visa acionar medidas preventivas apropriadas para evitar colisões.
    </details>
    <br>
    <details>
      <summary>📄 Relevância dos Dados</summary>
      A iniciativa depende de conjuntos de dados sintéticos e do mundo real que respeitam as leis de privacidade, incluindo o Regulamento Geral sobre a Proteção de Dados (GDPR), garantindo a relevância e a conformidade legal dos dados para o treinamento de modelos robustos de aprendizado de máquina.
    </details>
    <br>
    <details>
      <summary>📄 Identificação do Caso de Uso</summary>
      O caso de uso primário gira em torno da integração deste sistema de detecção em mecanismos de segurança veicular, fornecendo alertas em tempo real e automatizando sistemas de frenagem para prevenir colisões.
    </details>
    <br>
    <details>
      <summary>📄 Análise de ROI</summary>
      A implementação desta tecnologia poderia reduzir significativamente o risco de acidentes, diminuindo os custos de seguro e potencialmente salvando vidas. O retorno sobre o investimento se estende além das economias financeiras, englobando benefícios sociais através do aumento da segurança nas estradas.
    </details>
    <br>
    <details>
      <summary>📄 Engajamento dos Stakeholders</summary>
      Os stakeholders-chave incluem fabricantes de veículos, companhias de seguro, órgãos regulatórios e usuários finais. Suas contribuições são cruciais para refinar os objetivos do projeto e garantir que a solução atenda às diversas necessidades e esteja em conformidade com os padrões da indústria.
    </details>
    <br>
    <details>
      <summary>📄 Especificação de Requisitos</summary>
      As especificações incluem alta precisão na detecção de objetos sob várias condições ambientais, latência mínima para processamento em tempo real e compatibilidade com sistemas veiculares existentes. O modelo também deve ser leve para implantação em dispositivos de borda, como o Raspberry Pi.
    </details>
    <br>
    <details>
      <summary>📄 Avaliação de Tecnologia</summary>
      Ao avaliar as tecnologias disponíveis, o TensorFlow Lite se destaca por sua capacidade de executar modelos de deep learning em dispositivos de borda de forma eficiente. Ele oferece a eficiência computacional necessária e suporta os requisitos do projeto para processamento em tempo real.
    </details>
    <br>
    A fase de entendimento do problema estabelece, assim, uma sólida fundação para o projeto AssistenteSeguro FreioAntiColisão, direcionando as etapas subsequentes com um planejamento estratégico e metas claras, visando a maximização da segurança veicular através da inovação em detecção baseada em IA.
  </details> <!-- Fechamento da seção "01 - ENTENDIMENTO DO PROBLEMA" -->
  <br>
  <!-- Início da seção "02 - MINERAÇÃO DE DADOS" -->
  <details>
    <summary><h3>02 - MINERAÇÃO DE DADOS</h3></summary>
    <p align="center">
      <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/f2a46085-ceef-46e6-aa71-81ca3923698e" alt="fusca_foto_ic" width="250">
    </p>
    O processo de mineração de dados no projeto AssistenteSeguro FreioAntiColisão é uma etapa crucial para compreender e extrair informações valiosas a partir dos dados coletados. Ao explorar profundamente os dados disponíveis, buscamos identificar padrões, relações e características que serão fundamentais para o treinamento eficaz do nosso sistema de detecção. A seguir, detalhamos os componentes essenciais desta fase:
    <br><br>
    <details>
      <summary>📄 Padrões de Reconhecimento de Objetos</summary>
      Utilizando técnicas de aprendizado de máquina, o sistema aprende padrões associados à presença de "Murilo" versus outras entidades no campo visual.
    </details>
    <br>
    <details>
      <summary>📄 Agrupamento de Imagens</summary>
      Para aumentar a eficiência do modelo, as imagens são agrupadas com base na semelhança. Esta abordagem ajuda no manuseio de grandes quantidades de dados ao agrupar imagens similares, melhorando assim o processo de aprendizagem ao focar em características distintas dentro de cada grupo.
    </details>
    <br>
    <details>
      <summary>📄 Detecção de Relacionamento Visual</summary>
      O sistema é projetado para entender e interpretar relacionamentos entre diferentes objetos dentro de uma imagem. Por exemplo, distinguir entre "Murilo" e "Outros" em vários contextos e configurações espaciais, aumentando a aplicabilidade do modelo em cenários do mundo real.
    </details>
    <br>
      A mineração de dados, portanto, é uma fase de preparação indispensável que equipa o projeto AssistenteSeguro FreioAntiColisão com o conhecimento e a capacidade de reconhecer e interpretar eficientemente as nuances visuais. Por meio desta etapa, estabelecemos uma base sólida para o treinamento do nosso modelo, garantindo que ele esteja bem-preparado para lidar com os desafios de detecção em cenários reais, reforçando assim a segurança veicular por meio da inovação tecnológica.
    <!-- Insira o conteúdo da seção "02 - ENTENDIMENTO DO PROBLEMA" aqui -->
  </details>
    <br>
  <!-- Início da seção "03 - PRÉ-PROCESSAMENTO DE DADOS" -->
  <details>
  <summary><h3>03 - PRÉ-PROCESSAMENTO DE DADOS</h3></summary>
    <p align="center">
      <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/995f23d8-e452-474a-b1a0-17394f9427f3" alt="fusca_foto_ic" width="250">
    </p>
  A fase de pré-processamento é fundamental na preparação dos dados de imagem brutos para treinamento eficaz do modelo, envolvendo diversas etapas críticas:
  <br><br>
  <details>
    <summary>📄 Redimensionamento</summary>
    As imagens são redimensionadas para dimensões uniformes para garantir consistência no tamanho dos dados de entrada para o modelo. Esta uniformidade é crucial para o processamento eficiente e aprendizado da rede neural a partir do conjunto de dados. No projeto, imagens dos diretórios "Murilo_Original_Bruto" e "Outros_Sintetico_Bruto" são redimensionadas para uma resolução padrão, facilitando o processamento e análise eficazes.
  </details>
  <br>
  <details>
    <summary>📄 Aumento</summary>
    Para melhorar a robustez do modelo contra o overfitting e aumentar sua capacidade de generalização, técnicas de aumento de dados são aplicadas. Isso inclui rotacionar, espelhar e escalar imagens para introduzir uma maior variedade de variabilidade de dados. A fase "S4_Argumentacao_Renomeamento" dentro do pipeline Murilo exemplifica isso, onde imagens são aumentadas para criar amostras adicionais de treinamento.
  </details>
  <br>
  <details>
    <summary>📄 Espelhamento</summary>
    Como parte do aumento de dados, imagens são espelhadas horizontal ou verticalmente para simular diferentes perspectivas e ângulos, aumentando a diversidade do conjunto de dados de treinamento.
  </details>
  <br>
  <details>
    <summary>📄 Deformação</summary>
    As imagens podem ser ligeiramente deformadas para simular diferentes ângulos de câmera e perspectivas, introduzindo mais variabilidade no conjunto de dados sem a necessidade de coletar novos dados.
  </details>
  <br>
  <details>
    <summary>📄 Limpeza</summary>
    O conjunto de dados é meticulosamente limpo para remover quaisquer dados irrelevantes ou enganosos que possam impactar negativamente o processo de aprendizado do modelo. Este passo envolve filtrar imagens que não contribuem para a compreensão do modelo de "Murilo" e "Outros", assegurando a qualidade e relevância do conjunto de dados.
  </details>
  <br>
  <details>
    <summary>📄 Seleção</summary>
    Um processo seletivo é utilizado para escolher as imagens mais representativas e diversas para o conjunto de treinamento, garantindo um conjunto de dados abrangente que encapsula uma ampla gama de cenários em que "Murilo" e "Outros" podem aparecer.
  </details>
  <br>
  A fase de pré-processamento é meticulosamente projetada para otimizar o conjunto de dados para a fase subsequente de treinamento, garantindo que o modelo seja exposto a dados de alta qualidade e variados que encapsulem a complexidade dos cenários do mundo real com os quais se deparará.
</details>
  <br>
<!-- Início da seção "04 - ANOTAÇÃO DE DADOS" -->
<details>
  <summary><h3>04 - ANOTAÇÃO DE DADOS</h3></summary>
    <p align="center">
      <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/997938c6-1806-4eb7-83d9-1b1190464e2e" alt="fusca_foto_ic" width="250">
    </p>
  A anotação de dados é um processo crucial no projeto AssistenteSeguro FreioAntiColisão, assegurando que o modelo compreenda precisamente o contexto e conteúdo de cada imagem. Esta etapa envolve várias tarefas meticulosas:
  <br><br>
  <details>
    <summary>📄 Anotação de Texto</summary>
    Isso envolve adicionar texto descritivo às imagens, identificando e rotulando os objetos de interesse dentro delas. No contexto deste projeto, anotações de texto podem especificar a presença de "Murilo" ou "Outros" na imagem, fornecendo um rótulo claro para o modelo aprender.
  </details>
  <br>
  <details>
    <summary>📄 Caixas Delimitadoras</summary>
    Caixas retangulares são desenhadas ao redor de cada instância de "Murilo" e "Outros" nas imagens. Essas caixas delimitadoras são cruciais para ensinar ao modelo onde o objeto está localizado na imagem e qual forma ele assume, focando a atenção do modelo em áreas específicas dentro dos dados visuais.
  </details>
  <br>
  <details>
    <summary>📄 Classificação</summary>
    Cada imagem ou objeto dentro de uma imagem é classificado em categorias pré-definidas. Para este projeto, as classificações primárias são "Murilo" e "Outros". Esta classificação binária simples é fundamental para o modelo entender quais objetos são de interesse primário.
  </details>
  <br>
  A anotação de dados estabelece a base para o modelo aprender com precisão a partir dos dados visuais. Ela transforma imagens brutas em um formato estruturado que o modelo de aprendizado de máquina pode entender e aprender, garantindo que o modelo seja bem treinado para identificar "Murilo" e "Outros" com precisão na fase de implantação.
</details>
 <br>
<!-- Início da seção "05 - TREINAMENTO DO MODELO" -->
<details>
  <summary><h3>05 - TREINAMENTO DO MODELO</h3></summary>
    <p align="center">
      <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/8bcc218c-112b-4a08-ae62-455e6db9b44f" alt="fusca_foto_ic" width="250">
    </p>
  O treinamento do modelo é um marco decisivo no desenvolvimento do projeto AssistenteSeguro FreioAntiColisão, onde as preparações meticulosas e os insights coletados nas fases anteriores são postos em prática. Este estágio transforma dados brutos e teorias em uma ferramenta pronta para salvar vidas, através da precisão e eficiência na detecção de possíveis colisões. Detalhamos abaixo os processos essenciais que compõem esta fase crítica:
  <br><br>
  <details>
    <summary>📄 Divisão de Dados</summary>
    O processo inicia com a organização dos dados em conjuntos específicos para treino, validação e teste, assegurando uma distribuição apropriada que facilita um aprendizado eficaz e uma avaliação precisa do modelo.
  </details>
  <br>
  <details>
    <summary>📄 Seleção do Modelo</summary>
    Utiliza-se a facilidade de escolher entre modelos pré-treinados disponíveis no TensorFlow Object Detection Model Zoo, permitindo o aproveitamento de arquiteturas comprovadas e agilizando o início do treinamento.
  </details>
  <br>
  <details>
    <summary>📄 Configuração de Parâmetros de Treinamento</summary>
    Configurações essenciais como o número de passos de treinamento (num_steps) e o tamanho do lote (batch_size) são definidas, possibilitando a customização do processo de treinamento para atender às necessidades específicas do projeto.
  </details>
  <br>
  <details>
    <summary>📄 Uso de TensorBoard para Monitoramento</summary>
    A integração com o TensorBoard permite o monitoramento do progresso do treinamento em tempo real, fornecendo insights valiosos sobre o desempenho do modelo, a evolução da perda e outras métricas relevantes.
  </details>
  <br>
  <details>
    <summary>📄 Avaliação de Performance e mAP</summary>
    Ao final do treinamento, o modelo é avaliado utilizando imagens de teste para inferência, seguido pelo cálculo do mAP (mean Average Precision), oferecendo uma métrica quantitativa da precisão do modelo.
  </details>
  <br>
  <details>
    <summary>📄 Exportação para TensorFlow Lite</summary>
    O modelo treinado é então convertido para o formato TensorFlow Lite, otimizando-o para implantação eficiente em dispositivos de borda, preparando o caminho para sua utilização em aplicações reais e cenários de detecção de objetos.
  </details>
  <br>
  Ao final do treinamento do modelo, solidificamos o coração tecnológico do AssistenteSeguro FreioAntiColisão, capacitando-o a realizar sua missão crítica de identificar ameaças de colisão e ativar medidas preventivas. Este passo conclui a transição de dados e teorias em uma aplicação prática, que promete transformar o panorama da segurança veicular através do poder da detecção baseada em IA.
</details>
 <br>
<!-- Início da seção "06 - AVALIAÇÃO E OTIMIZAÇÃO - (SOON)" -->
<!-- Início da seção "06 - AVALIAÇÃO E OTIMIZAÇÃO - (SOON)" -->
  <details>
    <summary><h3>06 - AVALIAÇÃO E OTIMIZAÇÃO - (SOON)</h3></summary>
    <br><br>
    <!-- Conteúdo de "06 - AVALIAÇÃO E OTIMIZAÇÃO" aqui -->
  </details> <!-- Fechamento correto da seção "06 - AVALIAÇÃO E OTIMIZAÇÃO" -->

  <br> <!-- Espaçamento opcional entre as seções -->
  
  <!-- Início da seção "07 - IMPLEMENTAÇÃO E MONITORAMENTO - (SOON)" -->
  <details>
    <summary><h3>07 - IMPLEMENTAÇÃO E MONITORAMENTO - (SOON)</h3></summary>
    <br><br>
    <!-- Conteúdo de "07 - IMPLEMENTAÇÃO E MONITORAMENTO" aqui -->
  </details> <!-- Correto: Esta tag fecha "07 - IMPLEMENTAÇÃO E MONITORAMENTO" -->

<!-- A tag de fechamento de "📘 UTILIZAÇÃO" deve vir aqui, depois de todas as seções internas estarem fechadas -->
</details> <!-- Fechamento da seção "📘 UTILIZAÇÃO" -->
