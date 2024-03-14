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


<details>
  <summary><h2>📘 UTILIZAÇÃO</h2></summary>
  <p align="center">
    <img src="https://github.com/IM-NOT-AI/IM-NOT-AI/assets/113378671/f2e975e4-44f2-48d3-b5f6-0b7dcfb61944" alt="pipeline-root" />
  </p>

  <details>
    <summary><h3>01 - ENTENDIMENTO DO PROBLEMA</h3></summary>
    
  <details>
      <summary>📄 Definição do Objetivo</summary>
      O projeto, AssistenteSeguro FreioAntiColisão, é projetado para aumentar a segurança veicular desenvolvendo um sistema avançado de detecção capaz de identificar potenciais ameaças de colisão, focando especificamente em reconhecer "Murilo" e "Outros". Esta classificação binária visa acionar medidas preventivas apropriadas para evitar colisões.
    </details>

  <details>
      <summary>📄 Relevância dos Dados</summary>
      A iniciativa depende de conjuntos de dados sintéticos e do mundo real que respeitam as leis de privacidade, incluindo o Regulamento Geral sobre a Proteção de Dados (GDPR), garantindo a relevância e a conformidade legal dos dados para o treinamento de modelos robustos de aprendizado de máquina.
    </details>

  <details>
      <summary>📄 Identificação do Caso de Uso</summary>
      O caso de uso primário gira em torno da integração deste sistema de detecção em mecanismos de segurança veicular, fornecendo alertas em tempo real e automatizando sistemas de frenagem para prevenir colisões.
    </details>


  <details>
      <summary>📄 Análise de ROI</summary>
      O caso de uso primário gira em torno da integração deste sistema de detecção em mecanismos de segurança veicular, fornecendo alertas em tempo real e automatizando sistemas de frenagem para prevenir colisões.
    </details>


  <details>
      <summary>📄 Identificação do Caso de Uso</summary>
      A implementação desta tecnologia poderia reduzir significativamente o risco de acidentes, diminuindo os custos de seguro e potencialmente salvando vidas. O retorno sobre o investimento se estende além das economias financeiras, englobando benefícios sociais através do aumento da segurança nas estradas.
    </details>


  <details>
      <summary>📄 Engajamento dos Stakeholders</summary>
      Os stakeholders-chave incluem fabricantes de veículos, companhias de seguro, órgãos regulatórios e usuários finais. Suas contribuições são cruciais para refinar os objetivos do projeto e garantir que a solução atenda às diversas necessidades e esteja em conformidade com os padrões da indústria.
    </details>


  <details>
      <summary>📄 Especificação de Requisitos</summary>
      As especificações incluem alta precisão na detecção de objetos sob várias condições ambientais, latência mínima para processamento em tempo real e compatibilidade com sistemas veiculares existentes. O modelo também deve ser leve para implantação em dispositivos de borda, como o Raspberry Pi.
    </details>


  <details>
      <summary>📄 Avaliação de Tecnologia</summary>
      Ao avaliar as tecnologias disponíveis, o TensorFlow Lite se destaca por sua capacidade de executar modelos de deep learning em dispositivos de borda de forma eficiente. Ele oferece a eficiência computacional necessária e suporta os requisitos do projeto para processamento em tempo real.
    </details>

A fase de entendimento do problema estabelece, assim, uma sólida fundação para o projeto AssistenteSeguro FreioAntiColisão, direcionando as etapas subsequentes com um planejamento estratégico e metas claras, visando a maximização da segurança veicular através da inovação em detecção baseada em IA.
 
  </details>
</details>

