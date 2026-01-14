-> VISÃO GERAL

Este projeto implementa um pipeline ETL (Extract, Transform, Load) em Python, desenvolvido como parte do desafio da Santander Dev Week.

O foco principal é demonstrar, de forma prática, como dados podem ser extraídos, transformados e carregados, integrando boas práticas de Ciência de Dados e Inteligência Artificial, com atenção especial a problemas reais encontrados em projetos de dados.



-> OBJETIVOS DO PROJETO

Implementar um pipeline ETL completo em Python;
Trabalhar com dados estruturados em arquivos CSV;
Gerar mensagens personalizadas de marketing a partir dos dados;
Integrar IA generativa (OpenAI GPT) de forma opcional e segura;
Garantir compatibilidade com arquivos CSV gerados no Excel (encoding e separadores regionais).



-> PIPELINE ETL

Extract:
Leitura de dados a partir de arquivo CSV; 
Tratamento de encoding UTF-8 com BOM; 
Suporte a separador regional ;, comum em arquivos do Excel no Brasil.

Transform:
Criação de mensagens personalizadas de marketing; 
Integração opcional com Inteligência Artificial (OpenAI GPT); 
Implementação de fallback, garantindo que o pipeline execute mesmo sem acesso à API.

Load:
Escrita dos dados transformados em um novo arquivo CSV; 
Uso de encoding utf-8-sig, garantindo correta visualização de acentos no Excel.



-> COMO EXECUTAR O PROJETO

Pré-requisitos: Pré-requisitos

Instalar dependências: pip install -r requirements.txt

Executar pipeline: python main.py


-> RESULTADO ESPERADO

Após a execução, gerará o arquivo: data/output/messages.csv



-> TECNOLOGIAS UTILIZADAS

Python; 
Pandas; 
ETL (Extract, Transform, Load); 
OpenAI API.


-> APRENDIZADOS

Construção de pipelines ETL robustos
Tratamento correto de encoding e formatação de dados
Integração segura com IA generativa
Organização de projetos para portfólio profissional
