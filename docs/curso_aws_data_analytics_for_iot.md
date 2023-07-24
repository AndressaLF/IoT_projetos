# Curso AWS Data Analytics for IoT

<a name="ancora"></a>
## Índice
- [Conhecendo o curso](#conhecendo-curso)
- [Quais as soluções AWS estudadas e o que cada uma atende?](#solucoes-estudadas)
- [Explique três exemplos de atividades que você realizou no laboratório prático](#atividades-laboratorio-pratico)
- [Quais as principais lições apreendidas do curso?](#licoes-curso)

<a id="conhecendo-curso"></a>
# [Visão geral do curso](#conhecendo-curso)

O curso **Data Analytics** fornecido pela *AWS Academy* é focado no desenvolvimento das habilidade necessárias para análise de dados e big data utilizando as ferramentas e serviços fornecidos pela AWS.

O curso é subdivivido em nove laboratórios. O foco dos laboratórios está no desenvolvimento do conhecimento relacionado a utilização do conjunto de ferramentas da AWS. 

A lista dos laboratórios e seu resumo pode ser vista abaixo:

**1. Lab 1 - Store data in Amazon S3**

Neste laboratório, o objetivo é aprendem a armazenar dados na **Amazon S3** (Simple Storage Service), que é um dos serviço de armazenamento mais utilizados. O desenvolvimento desse laboratório requer a criação de um bucket do S3 usando o **AWS Management Console**, adição de usuário usando o **AWS Identity and Access Management (IAM)** a um grupo com total acesso ao Amazon S3, realizar o upload de arquivos para o Amazon S3 e executar consultas simples nos dados do Amazon S3 também são atividades realizadas ao longo desse laboratório.

**2. Lab 2 - Query Data in Amazon Athena**

Neste laboratório, o objetivo é aprendem a consultar e analisar dados armazenados no Amazon S3 usando o **Amazon Athena**, que é um serviço de consulta interativo de dados (estruturados, não estruturados e semiestruturados) sem servidor que permite executar consultas SQL diretamente em dados armazenados no S3, sem a necessidade de definir esquemas ou estruturas de dados.

**3. Lab 3 - Query data in Amazon S3 with Amazon Athena and AWS Glue**

Esse laboratório pode ser visto como uma continuação do laboratório anterior. Nesse laboratório o **Amazon Athena** continua ser explorado, juntamente do **AWS Glue**. O AWS Glue é um serviço de ETL (Extração, Transformação e Carga) que ajuda a descobrir, catalogar e transformar dados para facilitar a análise. Essa atividade se baseia na ideia de abstrair o esquema dos dados, apresentado no lab 2, para mostrar como usar o AWS Glue para inferir o esquema a partir dos dados.


**4. Lab 4 - Analyze Data with Amazon Redshift**

Este laboratório, ensina como analisar e consultar dados usando o **Amazon Redshift**. O uso do Redshift aborda um dos problemas centrais na análise de dados relacionado ao tratamento e armazenamento de um grande volume de dados. Nessa atividade é realizada a criação de cluster, consulta e carregamento de dados usando o Redshift.


**5. Lab 5 - Analyze Data with Amazon Sagemaker, Jupyter Notebooks and Bokeh**

Este laboratório explora o **Amazon Sagemaker**, o Jupyter Notebooks e o pacote Bokeh Python. O Amazon SageMaker é um serviço de aprendizado de máquina totalmente gerenciado e nesse laboratório ele será usado  para hospedar um notebook Jupyter.

**6. Lab 6 - Automate Loading Data with the AWS Data Pipeline**

O objetivo desse laboratório é aprender a automatizar o processo de carregamento de dados entre diferentes serviços da AWS usando o **AWS Data Pipeline**. Esse serviço permite que os dados sejam movimentados e transformados de forma programada e escalável, facilitando a integração entre diferentes fontes de dados.


**7. Lab 7 - Analyze Streaming Data with Amazon Kinesis Firehose, Amazon Elasticsearch and Kibana**

O objetivo desse laboratório é conhecer o **Amazon Kinesis Firehose**, que é um serviço que permite capturar e carregar dados de streaming em tempo real para armazenamento e análise. Nesse laboratório também são usados o ***Amazon Elasticsearch** e o **Kibana** para analisar e visualizar os dados de streaming de maneira interativa e em tempo real.

**8. Lab 8 - Analyze IoT Data with AWS IoT Analytics**

Neste laboratorio são apresentados o **AWS IoT Analytics** e o **AWS IoT Core**. O IoT Analytics permite coletar, processar e analisar grandes volumes de dados gerados por dispositivos IoT, ajudando a extrair insights valiosos e a tomar decisões inteligentes com base nesses dados. O IoT Core fornece conetividade entre dispositivos IoT e serviços AWS. Além dessas ferramentas, nesse laboratório usamos um script Python para simular o carregamento de dados no AWS IoT Core e realizamos consultas para analisar esses dados.


<a id="solucoes-estudadas"></a>
# [Quais as soluções AWS estudadas e o que cada uma atende?](#solucoes-estudadas)

O desenvolvimento dos oito laboratórios envolveu a utilização de sete soluções oferecidas pela AWS com foco no processamento de dados para IoT. 

Entre as muitas soluções disponibilizadas pela AWS, foram exploradas: 1) Amazon Athena, 2)Amazon Redshift, 3)Amazon S3, 4)AWS Glue, 5)AWS IoT Analytics e 6)Amazon Kinesis Data Firehose e 7) Amazon Elasticsearch Service (Amazon ES).

No contexto de soluções, as ferramentas oferecidas pela AWS podem se confundir e por isso explicarei de forma individual o que cada uma delas atende.

**1. Amazon Athena**

Amazon Athena é um serviço de análise interativo que permite consultar e analisar dados armazenados no Amazon S3 usando SQL padrão. Ele foi projetado para tornar a análise de dados mais rápida, simples e escalável, sem a necessidade de configurar e gerenciar um banco de dados ou infraestrutura complexa. Ele pode ser utilizado para analisar tanto dados não estruturados como dados semiestruturados armazenados no S3.

As principais ferramentas e recursos utilizados do Amazon Athena nos laboratórios foram: 

- AWS Management Console: O Amazon Athena pode ser acessado e configurado através da AWS Management Console, que é a interface web da AWS para gerenciar seus serviços em nuvem. Através do console, você pode criar bancos de dados, tabelas, executar consultas e visualizar os resultados.

- Query Editor: O Query Editor é uma ferramenta integrada ao console do Amazon Athena que permite escrever e executar consultas SQL diretamente na interface web. Com ele, você pode consultar os dados armazenados no Amazon S3 sem precisar instalar ou configurar softwares adicionais.

- Integração com Amazon S3:O Amazon Athena é altamente integrado com o Amazon S3, permitindo que você consulte dados diretamente nos arquivos armazenados no S3 sem a necessidade de carregá-los em um banco de dados ou data warehouse.

**2. Amazon Redshift**


**3. Amazon S3**
**4. AWS Glue**
**5. AWS IoT Analytics**
**6. Amazon Kinesis Data Firehose**
**7. Amazon Elasticsearch Service**










<a id="atividades-laboratorio-pratico"></a>
# [Explique três exemplos de atividades que você realizou no laboratório prático](#atividades-laboratorio-pratico)


<a id="licoes-curso"></a>
# [Quais as principais lições apreendidas do curso?](#licoes-curso)