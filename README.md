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
    <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/f2e975e4-44f2-48d3-b5f6-0b7dcfb61944" alt="pipeline-root" width="500" />
  </p>
  <br>
  <details>
    <summary><h3>01 - ENTENDIMENTO DO PROBLEMA</h3></summary>
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
    A fase de pré-processamento é fundamental na preparação dos dados de imagem brutos para treinamento eficaz do modelo, envolvendo diversas etapas críticas:
    <br><br>
    <b>Redimensionamento</b><br>
    As imagens são redimensionadas para dimensões uniformes para garantir consistência no tamanho dos dados de entrada para o modelo. Esta uniformidade é crucial para o processamento eficiente e aprendizado da rede neural a partir do conjunto de dados. No projeto, imagens dos diretórios "Murilo_Original_Bruto" e "Outros_Sintetico_Bruto" são redimensionadas para uma resolução padrão, facilitando o processamento e análise eficazes.
    <br><br>
    <b>Aumento</b><br>
    Para melhorar a robustez do modelo contra o overfitting e aumentar sua capacidade de generalização, técnicas de aumento de dados são aplicadas. Isso inclui rotacionar, espelhar e escalar imagens para introduzir uma maior variedade de variabilidade de dados. A fase "S4_Argumentacao_Renomeamento" dentro do pipeline Murilo exemplifica isso, onde imagens são aumentadas para criar amostras adicionais de treinamento.
    <br><br>
    <b>Espelhamento</b><br>
    Como parte do aumento de dados, imagens são espelhadas horizontal ou verticalmente para simular diferentes perspectivas e ângulos, aumentando a diversidade do conjunto de dados de treinamento.
    <br><br>
    <b>Deformação</b><br>
    As imagens podem ser ligeiramente deformadas para simular diferentes ângulos de câmera e perspectivas, introduzindo mais variabilidade no conjunto de dados sem a necessidade de coletar novos dados.
    <br><br>
    <b>Limpeza</b><br>
    O conjunto de dados é meticulosamente limpo para remover quaisquer dados irrelevantes ou enganosos que possam impactar negativamente o processo de aprendizado do modelo. Este passo envolve filtrar imagens que não contribuem para a compreensão do modelo de "Murilo" e "Outros", assegurando a qualidade e relevância do conjunto de dados.
    <br><br>
    <b>Seleção</b><br>
    Um processo seletivo é utilizado para escolher as imagens mais representativas e diversas para o conjunto de treinamento, garantindo um conjunto de dados abrangente que encapsula uma ampla gama de cenários em que "Murilo" e "Outros" podem aparecer.
    <br><br>
    A fase de pré-processamento é meticulosamente projetada para otimizar o conjunto de dados para a fase subsequente de treinamento, garantindo que o modelo seja exposto a dados de alta qualidade e variados que encapsulem a complexidade dos cenários do mundo real com os quais se deparará.
  </details>
</details> <!-- Fechamento da seção "📘 UTILIZAÇÃO" -->

